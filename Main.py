from animalType import AnimalType
from robot import Robot
import argparse
import sys
import time

def hunting_animal(animalType):
    robot = Robot()
    #robot.stop()
    #try:
    robot.anfangsfahrt()
    robot.looking_for_animal(animalType)
    robot.greifen()
    robot.weiterfahren()
    robot.unload_animal()
    robot.initial_state()
##    except Exception as e:
##        print(e)
##        print(sys.exc_info())
##        robot.stop()
    print("Done")

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--animal", help="animalType")
args = vars(ap.parse_args())


if not args.get("animal", False):
    print("no animal specified")
    sys.exit()

animal = args["animal"]

if not animal in AnimalType.__members__:
    print(animal + " is not a valid animal," +
          " please try TOMATO, DINO, TURTLE, FROG or TIGER")
    sys.exit()

animalType = AnimalType[animal]
print(animalType)

hunting_animal(animalType)
