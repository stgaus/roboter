import imutils
import cv2
import numpy as np

class FrameEditor():
    
    frame = None
    hsvFrame = None
    width = 800
    height = 450
    center = (400, 225)
    
    def __init__(self, frame):
        self.frame = frame

    def resize_frame(self, w, h):
        cut_left = int (round((w/8), 0))
        cut_right = int (round((w/8), 0))
        cut_top = int (round((h/4), 0))
        cut_bottom = int (round((h/14), 0))
        self.frame = cv2.resize(self.frame, (w, h))
        self.frame = self.frame[cut_top:h-cut_bottom, cut_left:w-cut_right]
        self.width = w - (cut_left + cut_right)
        self.height = h - (cut_top + cut_bottom)
        self.center = (int (round((self.width/2),0)), int (round((self.height/2),0)))
        return self.frame

    def convert_to_HSV(self):
        if self.frame is not None:
            self.hsvFrame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        return self.hsvFrame
    
    def draw_circle(self, x, y, radius, center):
        # only proceed if the radius meets a minimum size
        if radius > 10:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(self.frame, (int(x), int(y)), int(radius),
                       (0, 255, 255), 2)
            cv2.circle(self.frame, center, 5, (0, 0, 255), -1)

    def draw_rectangle(self, x, y, w, h):
        if x != None and y != None and w != None and h != None:
            cv2.rectangle(self.frame,(x,y),(x+w,y+h),(0,255,0),2)

    def draw_line(self, points, buffer):
        for i in range(1, len(points)):
            if points[i - 1] is None or points[i] is None:
                continue
            # draw the connecting lines
            cv2.line(self.frame, points[i - 1], points[i], (0, 0, 255), 1)

    def blur(self):
        #GaussianBlur(src, (width, height ->odd), sigmaX)
        #frame = cv2.GaussianBlur(frameEdit.frame, (17, 17), 0)
        self.frame = cv2.medianBlur(self.frame,7)
        #bilateralFilter(src, pixel neighborhood, sigmaColor, sigmaSpace) -->Härtere Kanten, aber langsamer
        #img = cv2.bilateralFilter(frameEdit.frame,14,100,75)
        return self.frame

    def draw_center_line(self):
        self.draw_line(((self.center[0] ,0), (self.center[0], self.height)), 64)
        



