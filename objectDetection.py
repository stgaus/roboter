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

                # Start time
                start = time.time()
                # construct the Video(webCam, path, buffer)
                #vid = Video(True, '', 64)
                vid = Video(False, 'test.h264', 64)
                #vid = Video(False, 'test-video2.mp4', 64)
                        
                colorScanner = ColorScanner(self.animal.minColorLimit, self.animal.maxColorLimit)

                # if a video path was not supplied, grab the reference to the webcam
                if vid.webCam:
                        camera = cv2.VideoCapture(0)

                # otherwise, grab a reference to the video file
                else:
                        camera = cv2.VideoCapture(vid.path)

                while True:
                        
                        # grab the current frame                        
                        (grabbed, frame) = camera.read()

                        # if we are viewing a video and we did not grab a frame,
                        # then we have reached the end of the video
                        if not vid.webCam and not grabbed:
                                break

                        frameEdit = FrameEditor(frame)
                        frame = frameEdit.resize_frame(800, 400)
                        frameEdit.blur()

                        img_hsv = frameEdit.convert_to_HSV()

                        mask = colorScanner.get_mask(img_hsv, self.animal.minColorLimit_second, self.animal.maxColorLimit_second, self.animal.dilateAmount)

                        #combine image and mask to show color on mask
                        frameEdit.frame = cv2.bitwise_and(frameEdit.frame, frameEdit.frame, mask=mask)

                        # find contours in the mask
                        contours = colorScanner.find_contours(mask)                        

                        #drawContours(image, contours, contourIdx ->| if negative, all contours are drawn |, color, thickness)
                        cv2.drawContours(frameEdit.frame, contours, -1, (255, 255, 0), 1)
                        
                        cont = colorScanner.unify_contours()                        

                        x, y, w, h = cv2.boundingRect(cont)
                        # draw a green rectangle to visualize the bounding rect
                        cv2.rectangle(frameEdit.frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                       
                        if x > self.animal.imageRange[0] and y > self.animal.imageRange[1]:                                
                                if w > self.animal.boundingRectangleSize[0] and h > self.animal.boundingRectangleSize[1]:
                                        print(self.animal.name + " is coming")
                                        if x + w/2 > (frameEdit.center[0] - 7) and x + w/2 < (frameEdit.center[0] + 7):
                                                print("i found " + self.animal.name)
                                                time.sleep(1)
                                else:
                                        if w > 30 and h > 30:
                                                print("maybe " + self.animal.name + " on the screen")

                        
                        frameEdit.draw_center_line()
                        frameEdit.draw_line(((0, self.animal.imageRange[1]), (frameEdit.width, self.animal.imageRange[1])), vid.buffer)
                        
                        cv2.imshow("Frame", frameEdit.frame)
                        cv2.imshow("Tresh", frame)
                        #cv2.imshow("Thresh", mask)
                        
                        key = cv2.waitKey(1) & 0xFF                        

                        # if the 'q' key is pressed, stop the loop
                        if key == ord("q"):
                                break

                # cleanup the camera and close any open windows
                camera.release()
                cv2.destroyAllWindows()
                        

