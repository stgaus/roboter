class Animal():

    name = "Animal"
    minColorLimit = (0,0,0)
    maxColorLimit = (0,0,0)
    minColorLimit_second = (0,0,0)
    maxColorLimit_second = (0,0,0)
    minEnclosingCircleRadius = 10
    boundingRectangleSize = (10, 10)
    imageRange = (0, 0)
    dilateAmount = 5
    
    def __init__(self):
        pass


class Frog(Animal):

    def __init__(self):
        Animal.__init__(self)
        Animal.name = "Frog"
        #Animal.minColorLimit = (44, 39, 0)
        #Animal.maxColorLimit = (85, 255, 255)
        Animal.minColorLimit = (28, 55, 0)
        Animal.maxColorLimit = (79, 255, 165)
        Animal.minEnclosingCircleRadius = 40
        Animal.boundingRectangleSize = (100, 150)
        Animal.imageRange = (0, 0)
        Animal.dilateAmount = 10
        #minLimit = np.array([50, 45, 0])
        #maxLimit = np.array([75, 255, 150])

class Tiger(Animal):

    def __init__(self):
        Animal.__init__(self)
        Animal.name = "Tiger"
        Animal.minColorLimit = (14, 90, 70)
        Animal.maxColorLimit = (18, 200, 140)
        Animal.minEnclosingCircleRadius = 40
        Animal.boundingRectangleSize = (100, 150)
        Animal.imageRange = (0, 0)
        Animal.dilateAmount = 14
        #minLimit1 = np.array([13, 150, 10])
        #maxLimit1 = np.array([18, 255, 80])

class Dino(Animal):

    def __init__(self):
        Animal.__init__(self)
        Animal.name = "Dino"
        #Animal.minColorLimit = (100, 140, 60)
        Animal.minColorLimit = (100, 70, 0)
        #Animal.maxColorLimit = (120, 255, 255)
        Animal.maxColorLimit = (120, 255, 100)
        Animal.minEnclosingCircleRadius = 30
        Animal.boundingRectangleSize = (70, 100)
        Animal.imageRange = (0, 120)
        Animal.dilateAmount = 10
        #minLimit = np.array([100, 30, 0])
        #maxLimit = np.array([120, 255, 255])

class Tomato(Animal):

    def __init__(self):
        Animal.__init__(self)
        Animal.name = "Tomato"
        Animal.minColorLimit = (0, 120, 30)
        Animal.maxColorLimit = (7, 255, 150)
        minColorLimit_second = (174, 150, 60)
        maxColorLimit_second = (184, 255, 135)
        Animal.minEnclosingCircleRadius = 50
        Animal.boundingRectangleSize = (85, 85)
        Animal.imageRange = (0, 150)
        Animal.dilateAmount = 8


class Turtle(Animal):

    def __init__(self):
        Animal.__init__(self)
        Animal.name = "Turtle"
        Animal.minColorLimit = (0, 20, 100)
        Animal.maxColorLimit = (100, 100, 210)
        #Animal.minColorLimit = (0, 20, 110)
        #Animal.maxColorLimit = (14, 100, 200)
        #minColorLimit_second = (0, 15, 140)
        #maxColorLimit_second = (20, 46, 255)
        Animal.minEnclosingCircleRadius = 30
        Animal.boundingRectangleSize = (30, 30)
        Animal.imageRange = (0, 300)
        Animal.dilateAmount = 5


##TOMATO:
##  r,g,b = 203, 31, 25                        
##  target_color = np.uint8([[[b, g, r]]])
##  print(target_color)
##  target_color_hsv = cv2.cvtColor(target_color, cv2.COLOR_BGR2HSV)
##  print(target_color_hsv)
##  target_color_h = target_color_hsv[0,0,0]
##  print(target_color_h)
##  tolerance = 2
##  minLimit = np.array([max(0, target_color_h - tolerance), 10, 10])
##  maxLimit = np.array([min(179, target_color_h + tolerance), 250, 250])


