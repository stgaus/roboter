from objectDetection import ObjectDetection
from animalType import AnimalType
import argparse
import sys


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

od = ObjectDetection(animalType)
od.search_animal()



