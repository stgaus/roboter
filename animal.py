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
        Animal.minColorLimit = (28, 100, 0) 
        Animal.maxColorLimit = (65, 255, 100)
        Animal.boundingRectangleSize = (0.25, 0.75) #(100, 150)
        Animal.imageRange = (0, 0.35)#in decimal percent
        Animal.dilateAmount = 4

class Tiger(Animal):

    def __init__(self):
        Animal.__init__(self)
        Animal.name = "Tiger"
        #Animal.minColorLimit = (11, 80, 70)
        #Animal.maxColorLimit = (23, 180, 130)
        Animal.minColorLimit = (10, 50, 40)
        Animal.maxColorLimit = (30, 200, 130)
        Animal.boundingRectangleSize = (0.1, 0.7) #(100, 150)
        Animal.imageRange = (0, 0.35)#in decimal percent
        Animal.dilateAmount = 10

class Dino(Animal):

    def __init__(self):
        Animal.__init__(self)
        Animal.name = "Dino"
        #Animal.minColorLimit = (97, 65, 0)
        #Animal.maxColorLimit = (117, 200, 100)
        Animal.minColorLimit = (100, 28, 52)
        Animal.maxColorLimit = (143, 169, 108)
        #Animal.minColorLimit = (45, 45, 23)
        #Animal.maxColorLimit = (100, 190, 100)
        #Animal.boundingRectangleSize =  (0.1, 0.7) #(70, 100)
        Animal.boundingRectangleSize = (0.15, 0.2) #(100, 150)
        Animal.imageRange = (0, 0.35)#in decimal percent
        Animal.dilateAmount = 13

class Tomato(Animal):

    def __init__(self):
        Animal.__init__(self)
        Animal.name = "Tomato"
        Animal.minColorLimit = (0, 120, 30)
        Animal.maxColorLimit = (7, 255, 150)
        Animal.minColorLimit_second = (174, 150, 60)
        Animal.maxColorLimit_second = (184, 255, 150)
        Animal.boundingRectangleSize = (0.1, 0.2) #(85, 85)
        Animal.imageRange = (0, 0.7)#in decimal percent
        Animal.dilateAmount = 3


class Turtle(Animal):

    def __init__(self):
        Animal.__init__(self)
        Animal.name = "Turtle"
        #Animal.minColorLimit = (6, 20, 45)
        #Animal.maxColorLimit = (30, 140, 150)
        Animal.minColorLimit = (3, 50, 48)
        Animal.maxColorLimit = (20, 187, 121)
        #Animal.minColorLimit = (20, 40, 80)
        #Animal.maxColorLimit = (30, 150, 100)
        #Animal.minColorLimit_second = (5, 65, 65)
        #Animal.maxColorLimit_second = (25, 135, 160)
        #RGB-WERTE:
        #Animal.minColorLimit = (30, 35, 80) 
        #Animal.maxColorLimit = (80, 95, 135)
        #Animal.minColorLimit_second = (120, 130, 175)
        #Animal.maxColorLimit_second = (180, 185, 200)
        Animal.boundingRectangleSize = (0.2, 0.7) #(30, 30)
        Animal.imageRange = (0, 0.4)#in decimal percent
        Animal.dilateAmount = 8

class Shelf(Animal):

    def __init__(self):
        Animal.__init__(self)
        Animal.name = "Shelf"
        Animal.minColorLimit = (35, 14, 140)
        Animal.maxColorLimit = (61, 44, 166)
        Animal.boundingRectangleSize = (0.2, 0.7) #(85, 85)
        Animal.imageRange = (0.3, 0.3, 0.5, 0.3)#in decimal percent #u,o,l,r
        Animal.dilateAmount = 3

