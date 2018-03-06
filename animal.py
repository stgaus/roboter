class Animal():

    name = "Animal"
    minColorLimit = (0,0,0)
    maxColorLimit = (0,0,0)
    minColorLimit_second = (0,0,0)
    maxColorLimit_second = (0,0,0)
    boundingRectangleSize = (10, 10)
    imageRange = (0, 0)#in decimal percent
    dilateAmount = 5
    
    def __init__(self):
        pass


class Frog(Animal):

    def __init__(self):
        Animal.__init__(self)
        Animal.name = "Frog"
        Animal.minColorLimit = (28, 120, 0) 
        Animal.maxColorLimit = (79, 255, 165)
        Animal.boundingRectangleSize = (0.15, 0.9) #(100, 150)
        Animal.imageRange = (0, 0.34)#in decimal percent
        Animal.dilateAmount = 10

class Tiger(Animal):

    def __init__(self):
        Animal.__init__(self)
        Animal.name = "Tiger"
        Animal.minColorLimit = (14, 90, 70)
        Animal.maxColorLimit = (18, 200, 140)
        Animal.boundingRectangleSize = (0.2, 0.9) #(100, 150)
        Animal.imageRange = (0, 0.4)#in decimal percent
        Animal.dilateAmount = 10

class Dino(Animal):

    def __init__(self):
        Animal.__init__(self)
        Animal.name = "Dino"
        Animal.minColorLimit = (100, 70, 0)
        Animal.maxColorLimit = (120, 200, 100)
        Animal.boundingRectangleSize =  (0.1, 0.7) #(70, 100)
        Animal.boundingRectangleSize = (0.1, 0.7) #(100, 150)
        Animal.imageRange = (0, 0.5)#in decimal percent
        Animal.dilateAmount = 13

class Tomato(Animal):

    def __init__(self):
        Animal.__init__(self)
        Animal.name = "Tomato"
        Animal.minColorLimit = (0, 120, 30)
        Animal.maxColorLimit = (7, 255, 150)
        Animal.minColorLimit_second = (174, 150, 60)
        Animal.maxColorLimit_second = (184, 255, 135)
        Animal.boundingRectangleSize = (0.1, 0.7) #(85, 85)
        Animal.imageRange = (0, 0.65)#in decimal percent
        Animal.dilateAmount = 3


class Turtle(Animal):

    def __init__(self):
        Animal.__init__(self)
        Animal.name = "Turtle"
        #Animal.minColorLimit = (0, 15, 65)
        #Animal.maxColorLimit = (10, 115, 190)
        Animal.minColorLimit = (20, 40, 90)
        Animal.maxColorLimit = (30, 65, 130)
        Animal.minColorLimit_second = (5, 65, 55)
        Animal.maxColorLimit_second = (25, 135, 95)
        #RGB-WERTE:
        #Animal.minColorLimit = (30, 35, 80) 
        #Animal.maxColorLimit = (80, 95, 135)
        #Animal.minColorLimit_second = (120, 130, 175)
        #Animal.maxColorLimit_second = (180, 185, 200)
        Animal.boundingRectangleSize = (0.2, 0.8) #(30, 30)
        Animal.imageRange = (0, 0.64)#in decimal percent
        Animal.dilateAmount = 8

