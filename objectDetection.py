# import the necessary packages
from collections import deque
import numpy as np
import imutils
import cv2
from video import Video
from colorScanner import ColorScanner
from frameEditor import FrameEditor
from animalType import AnimalType
from animal import Animal, Frog, Tomato, Tiger, Turtle, Dino
from consts import Consts
import signal
import time

class ObjectDetection():

        animal = None

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

        def search_animal(self):
                # construct the Video(webCam, path, buffer)
                #vid = Video(True, '', 64)
                #vid = Video(False, 'test.h264', 64)
                vid = Video(False, 'final_video.mp4', 64)
                #vid = Video(False, 'test-video1.mp4', 64)
                        
                colorScanner = ColorScanner(self.animal.minColorLimit, self.animal.maxColorLimit)

                # if a video path was not supplied, grab the reference to the webcam
                if vid.webCam:
                        camera = cv2.VideoCapture(0)

                # otherwise, grab a reference to the video file
                else:
                        camera = cv2.VideoCapture(vid.path)

                # Start time
                start = time.time()
                couuunt=0
                while True: #couuunt < 200:
                        
                        # grab the current frame                        
                        (grabbed, frame) = camera.read()

                        # if we are viewing a video and we did not grab a frame,
                        # then we have reached the end of the video
                        if not vid.webCam and not grabbed:
                                break

                        frameEdit = FrameEditor(frame)
                        frame = frameEdit.resize_frame(Consts.IMG_WIDTH, Consts.IMG_HEIGHT, self.animal.imageRange)
                        frameEdit.blur()

                        img_hsv = frameEdit.convert_to_HSV()

                        mask = colorScanner.get_mask(img_hsv, self.animal.minColorLimit_second, self.animal.maxColorLimit_second, self.animal.dilateAmount)

                        #combine image and mask to show color on mask
                        frameEdit.combine_frame_and_mask(mask)

                        contours = colorScanner.find_contours(mask)
                        
                        cont = colorScanner.unify_contours()

                        #drawContours(image, contours, contourIdx ->| if negative, all contours are drawn |, color, thickness)
                        cv2.drawContours(frameEdit.frame, cont, -1, (255, 255, 0), 2)

                        x, y, w, h = cv2.boundingRect(cont)
                        # draw a green rectangle to visualize the bounding rect
                        cv2.rectangle(frameEdit.frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                                                      
                        if self.is_animal_on_screen(frameEdit.width, frameEdit.height, w, h):
                                print(self.animal.name + " is coming")
                                #return 1
                                if self.is_animal_in_center(frameEdit.center[0], (x + w/2)):
                                        print("i found " + self.animal.name)
                                        time.sleep(0.5)
                                        #return 2
                        #else return 0
                        
                        frameEdit.draw_center_line()
                        
                        cv2.imshow("Frame", frameEdit.frame)
                        cv2.imshow("Tresh", frame)
                        couuunt+= 1
                        
                        key = cv2.waitKey(1) & 0xFF                        

                        # if the 'q' key is pressed, stop the loop
                        if key == ord("q"):
                                break

                # cleanup the camera and close any open windows
                camera.release()
                cv2.destroyAllWindows()

                
                # End time
                end = time.time()

                # Time elapsed
                seconds = end - start
                print("Time taken : {0} seconds".format(seconds))
                         
                # Calculate frames per second
                fps  = couuunt / seconds;
                print("Estimated frames per second : {0}".format(fps))

        def is_animal_on_screen(self, frame_width, frame_height, rect_w, rect_h):
                if rect_w > (frame_width * self.animal.boundingRectangleSize[0]) and rect_h > (frame_height * self.animal.boundingRectangleSize[1]):
                        return True
                return False

        def is_animal_in_center(self, frame_center, rect_horizontal_center):
                if rect_horizontal_center > (frame_center - Consts.CENTER_TOLERANCE) and rect_horizontal_center < (frame_center + Consts.CENTER_TOLERANCE):
                        return True
                return False
                        

