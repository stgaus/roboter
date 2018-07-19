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
from animal import Animal, Frog, Tomato, Tiger, Turtle, Dino, Shelf
from consts import Consts
import signal
import time

class ObjectDetection():

        animal = None
        seen_animal_counter = 0

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
                if animalType == AnimalType.SHELF:
                        self.animal = Shelf()

        def search_animal(self, frame_no, animal_on_screen):
                returnValue = 0
                # construct the Video(webCam, path, buffer)
                #vid = Video(True, '', 64)
                #vid = Video(False, 'final_video.mp4', 64)
                #vid = Video(False, 'test.h264', 64)
                vid = Video(False, 'gutesVid2.h264', 64)
                #vid = Video(False, 'test-video1.mp4', 64)
                        
                colorScanner = ColorScanner(self.animal.minColorLimit, self.animal.maxColorLimit)

                # if a video path was not supplied, grab the reference to the webcam
                if vid.webCam:
                        camera = VideoStream(usePiCamera=-1 > 0).start()
                        #time.sleep(2.0)
                        #camera = WebcamVideoStream(src=0).start()
                        #camera = cv2.VideoCapture(0)
                        fps = FPS().start()

                # otherwise, grab a reference to the video file
                else:
                        camera = cv2.VideoCapture(vid.path)

                # Start time
                fps = FPS().start()
                while True:
                        # grab the current frame                        
                        (grabbed, frame) = camera.read()
                        #frame = camera.read()                        
                        #if camera.get(1) < frame_no:
                        #        continue
                        #simulates slow_down_motor:
                        #if animal_on_screen == True:
                        time.sleep(0.1)
                        
                        # if we are viewing a video and we did not grab a frame,
                        # then we have reached the end of the video
                        if not vid.webCam and not grabbed:
                                break
                        (rows,cols,shit) = frame.shape
                        M = cv2.getRotationMatrix2D((cols/2,rows/2), 270, 1)
                        dst = cv2.warpAffine(frame, M, (cols, rows))
                        frame = dst
                        frameEdit = FrameEditor(frame)
                        frame = frameEdit.resize_frame(Consts.IMG_WIDTH, Consts.IMG_HEIGHT, self.animal.imageRange)
                        frameEdit.blur()

                        img_hsv = frameEdit.convert_to_HSV()

                        mask = colorScanner.get_mask(img_hsv, self.animal.minColorLimit_second, self.animal.maxColorLimit_second, self.animal.dilateAmount)

                        #combine image and mask to show color on mask
                        frameEdit.combine_frame_and_mask(mask)

                        contours = colorScanner.find_contours(mask)
                        
                        #cont = colorScanner.unify_contours()
                        #cont = colorScanner.get_max_contours()
                        cont = colorScanner.get_max_contour()

                        #drawContours(image, contours, contourIdx ->| if negative, all contours are drawn |, color, thickness)
                        cv2.drawContours(frameEdit.frame, cont, -1, (255, 255, 0), 2)

                        x, y, w, h = cv2.boundingRect(cont)
                        #print(w, h)
                        # draw a green rectangle to visualize the bounding rect
                        cv2.rectangle(frameEdit.frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        #print(frameEdit.width, frameEdit.height)                              
                        if self.is_animal_on_screen(frameEdit.width, frameEdit.height, w, h):
                                if animal_on_screen == False:                                        
                                        self.seen_animal_counter += 1
                                        if self.seen_animal_counter > Consts.SEEN_ANIMAL_COUNTER:
                                                print("animal on screen")
                                                self.animal = Shelf()#return (1, 0)#camera.get(1))
                                                colorScanner = ColorScanner(self.animal.minColorLimit, self.animal.maxColorLimit)
                                                animal_on_screen = True
                                if self.is_animal_in_center(frameEdit.center[0], (x + w/2)):
                                        #frame_no = camera.get(1)
                                        camera.release()
                                        #camera.stop()
                                        fps.stop()
                                        print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
                                        cv2.destroyAllWindows()
                                        return (2, 0)
                        
                        frameEdit.draw_center_line()
                        frameEdit.draw_check_line(int(round(frameEdit.center[0]/2, 0)))
                        
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
                
                return (-1, 0)#camera.get(1))


        def is_animal_on_screen(self, frame_width, frame_height, rect_w, rect_h):
                if rect_w > (frame_width * self.animal.boundingRectangleSize[0]) and rect_h > (frame_height * self.animal.boundingRectangleSize[1]):
                        return True
                return False

        def is_animal_in_center(self, frame_center, rect_horizontal_center):
                if rect_horizontal_center > (frame_center + (frame_center/2) - Consts.CENTER_TOLERANCE) and rect_horizontal_center < (frame_center + (frame_center/2) + Consts.CENTER_TOLERANCE):
                        return True
                return False
                        

