import numpy as np
import imutils
import cv2
from video import Video
#from imutils.video.pivideostream import PiVideoStream
from imutils.video import VideoStream
#from imutils.video import FPS
#from picamera.array import PiRGBArray
#from picamera import PiCamera
from imutils.video import FPS
from colorScanner import ColorScanner
from frameEditor import FrameEditor
from animalType import AnimalType
from animal import Animal, Frog, Tomato, Tiger, Turtle, Dino
from consts import Consts
import signal
import time
#from robot import Robot

class ObjectDetection():

        animal = None
        seen_animal_counter = 0
        animal_in_center = False
        cut_right = None
        cut_left = None

        def __init__(self, animalType):
                if animalType == AnimalType.DINO:
                        self.animal = Dino()
                if animalType == AnimalType.TOMATO:
                        self.animal = Tomato()
                if animalType == AnimalType.TURTLE:
                        self.animal = Turtle()
                if animalType == AnimalType.FROG:
                        self.animal = Frog()
                if animalType == AnimalType.TIGER:
                        self.animal = Tiger()

        def search_animal(self, frame_no, animal_on_screen, motor, camera, robot):
                found_animal = False
                # construct the Video(webCam, path, buffer)
                #vid = Video(True, '', 64)
                vid = Video(False, 'FinalVid2.h264', 64)
                        
                colorScanner = ColorScanner(self.animal.minColorLimit, self.animal.maxColorLimit)
                fps = FPS().start()
                # if a video path was not supplied, grab the reference to the webcam
                if vid.webCam:
                        camera.start()                        

                # otherwise, grab a reference to the video file
                else:
                        camera = cv2.VideoCapture(vid.path)

                # Start time
                while True:
                        # grab the current frame                        
                        (grabbed, frame) = camera.read()
                        #frame = camera.read()
                        #(rows,cols,shit) = frame.shape
                        #M = cv2.getRotationMatrix2D((cols/2,rows/2), 270, 1)
                        #dst = cv2.warpAffine(frame, M, (cols, rows))
                        #frame = dst
                        
                        # if we are viewing a video and we did not grab a frame,
                        # then we have reached the end of the video
                        #if not vid.webCam and not grabbed:
                        #        return (-1, camera.get(1))

                        frameEdit = FrameEditor(frame)
                        frame = frameEdit.resize_frame(Consts.IMG_WIDTH, Consts.IMG_HEIGHT, self.animal.imageRange, self.cut_right, self.cut_left)
                        frameEdit.blur()

                        img_hsv = frameEdit.convert_to_HSV()

                        mask = colorScanner.get_mask(img_hsv, self.animal.minColorLimit_second, self.animal.maxColorLimit_second, self.animal.dilateAmount)

                        #combine image and mask to show color on mask
                        frameEdit.combine_frame_and_mask(mask)

                        contours = colorScanner.find_contours(mask)
                        
                        if animal_on_screen == True:
                                cont = colorScanner.get_max_contours()
                                #cont = colorScanner.unify_contours()
                        else:
                                cont = colorScanner.get_max_contour()
                        

                        #drawContours(image, contours, contourIdx ->| if negative, all contours are drawn |, color, thickness)
                        cv2.drawContours(frameEdit.frame, cont, -1, (255, 255, 0), 2)
                        x, y, w, h = cv2.boundingRect(cont)
                        
                        # draw a green rectangle to visualize the bounding rect
                        cv2.rectangle(frameEdit.frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        cv2.imwrite("last_image.png", frameEdit.frame)
                        if self.animal_in_center == False:
                                if self.is_animal_on_screen(frameEdit.width, frameEdit.height, w, h):
                                        if animal_on_screen == False:                                        
                                                self.seen_animal_counter += 1
                                                if self.seen_animal_counter > Consts.SEEN_ANIMAL_COUNTER:
                                                        print("animal on screen")
                                                        animal_on_screen = True
                                                        time.sleep(0.5)
                                                        #motor.motor_stop_light()
                                                        #robot.irCallback_Left.cancel()
                                                        #robot.irCallback_Right.cancel()
                                                        self.animal_in_center = True
                        else:
                                #frameEdit.frame = frameEdit.frame[0:frameEdit.height, 0:370]  
                                self.cut_right = 400
                                self.cut_left = 5
                                if self.is_animal_really_in_center(frameEdit.center[0], (x + w/2)):
                                        print("really in center")  
                                        cv2.destroyAllWindows()
                                        #camera.stop()
                                        camera.release()
                                        return (True, frame_no)                                                
                                elif self.is_animal_on_left(frameEdit.center[0], (x + w/2)):
                                        print("animal left - drive back")
                                        t_drive = time.time() + 0.1
                                        while time.time() < t_drive:
                                                test=1
                                                #motor.motor_backward(Consts.MOTOR_WHEELS_FREQUENCY_CORRECT
                                                #                        ,Consts.MOTOR_WHEELS_DUTYCYLCE_CORRECT)
                                        #motor.motor_stop_light()
                                elif self.is_animal_on_right(frameEdit.center[0], (x + w/2)):
                                        print("animal right - drive forward")
                                        t_drive = time.time() + 0.1
                                        while time.time() < t_drive:
                                                test=1
                                                #motor.motor_forward(Consts.MOTOR_WHEELS_FREQUENCY_CORRECT
                                                #        ,Consts.MOTOR_WHEELS_DUTYCYLCE_CORRECT)
                                        #motor.motor_stop_light()
                                else:
                                        print("not on screen - drive back")
                                        t_drive = time.time() + 0.3
                                        while time.time() < t_drive:
                                                test=1
                                                #motor.motor_backward(Consts.MOTOR_WHEELS_FREQUENCY_CORRECT
                                                #        ,Consts.MOTOR_WHEELS_DUTYCYLCE_CORRECT)
                                        #motor.motor_stop_light()
                                      

                        
                        #frameEdit.draw_center_line()
                        frameEdit.draw_check_line(frameEdit.center[0] + 7)
                        frameEdit.draw_check_line(frameEdit.center[0] - 7)
                        
                        cv2.imshow("Frame", frameEdit.frame)
                        cv2.imshow("Tresh", frame)
                        
                        key = cv2.waitKey(1) & 0xFF                        

                        # if the 'q' key is pressed, stop the loop
                        if key == ord("q"):
                                break
                        fps.update()

                # cleanup the camera and close any open windows
                fps.stop()
                print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

                #camera.stop()
                camera.release()
                cv2.destroyAllWindows()
                
                return (False, 0)


        def is_animal_on_screen(self, frame_width, frame_height, rect_w, rect_h):
                if rect_w > (frame_width * self.animal.boundingRectangleSize[0]) and rect_h > (frame_height * self.animal.boundingRectangleSize[1]):
                        return True
                return False

        def is_animal_in_center(self, frame_center, rect_horizontal_center):
                if rect_horizontal_center > (frame_center - Consts.CENTER_TOLERANCE) and rect_horizontal_center < (frame_center + Consts.CENTER_TOLERANCE):
                        return True
                return False

        def is_animal_on_left(self, frame_center, rect_horizontal_center):
                if rect_horizontal_center < (frame_center - 7):
                        return True
                return False

        def is_animal_on_right(self, frame_center, rect_horizontal_center):
                if rect_horizontal_center > (frame_center + 7):
                        return True
                return False

        def is_animal_really_in_center(self, frame_center, rect_horizontal_center):
                if rect_horizontal_center > (frame_center - 7) and rect_horizontal_center < (frame_center + 7):
                        return True
                return False        

