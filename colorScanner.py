import cv2
import numpy as np
from Consts import consts

class ColorScanner():
    
    minLimit = (0, 0, 0)
    maxLimit = (0, 0, 0)
    contours = None
    
    def __init__(self, minLimit, maxLimit):
        self.minLimit = minLimit
        self.maxLimit = maxLimit

    def get_mask(self, hsv, minLimit1, maxLimit1, dilateAmount):
        mask = cv2.inRange(hsv, self.minLimit, self.maxLimit)
        if minLimit1 is not None and maxLimit1 is not None:
            mask1 = cv2.inRange(hsv, minLimit1, maxLimit1)
            # join masks
            mask = mask + mask1
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=dilateAmount)
        return mask

    def find_contours(self, mask):
        if mask is not None:
            self.contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                             cv2.CHAIN_APPROX_SIMPLE)[-2]
        return self.contours

    def find_if_close(self, cnt1,cnt2):
        row1,row2 = cnt1.shape[0],cnt2.shape[0]
        for i in range(row1):
            for j in range(row2):
                dist = np.linalg.norm(cnt1[i]-cnt2[j])
                if abs(dist) < consts.DISTANCE_FOR_CLOSE_CONTOURS :
                    return True
                elif i==row1-1 and j==row2-1:
                    return False

    def unify_contours(self):
        cont = None
        status = np.zeros((len(self.contours),1))
        for i,cnt1 in enumerate(self.contours):
            x = i    
            if i != len(self.contours)-1:
                for j,cnt2 in enumerate(self.contours[i+1:]):
                    x = x+1
                    dist = self.find_if_close(cnt1,cnt2)
                    if dist == True:
                        val = min(status[i],status[x])
                        status[x] = status[i] = val
                    else:
                        if status[x]==status[i]:
                            status[x] = i+1        
        
        if len(status) > 0:
            maximum = int(status.max())+1
            for i in range(maximum):
                pos = np.where(status==i)[0]
                if pos.size != 0:
                    cnt = np.vstack(self.contours[i] for i in pos)
                    if cont is None:
                        cont = cnt
                    if len(cnt) > len(cont):
                        cont = cnt
        return cont

    def get_max_contour(self):
        cont = None
        if len(self.contours) > 0:
            cont = max(self.contours, key=cv2.contourArea)
        return cont


            

