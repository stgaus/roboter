#import pigpio
import time
from antrieb import Antrieb
from infrared import Infrared
from greifer import Greifer
from consts import Consts
from objectDetection1 import ObjectDetection

class Robot():

    motor = None
    ir = None
    pi = None
    gripper = None
    
    def __init__(self):
        self.motor = Antrieb()
        self.ir = Infrared()
##        self.pi = pigpio.pi()
        self.gripper = Greifer()
        
    #Funktion für die Anfangsfahrt
    def anfangsfahrt(self):
        #cb1 = pi.callback(18, pigpio.EITHER_EDGE, self.ir.ir_signal_changed_left)
        #cb2 = pi.callback(19, pigpio.EITHER_EDGE, self.ir.ir_signal_changed_right)
        print("initialize ir_callback")
        #self.motor.motor_forward([duty])
        print("drive forward")       

    def looking_for_animal(self, animalType):
        returnValue = 0
        while True:
            #scannt für Tier
            if returnValue == 0:
                od = ObjectDetection(animalType)
                (returnValue, frame_no) = od.search_animal(0, False)
                
            #beendet Schleife, wenn Tier gefunden wird
            if returnValue == 2:
                print("i found " + animalType.name)
                break

            #reduziert speed, wenn Tier auf dem Screen ist
            if returnValue == 1:
                print(animalType.name + " is coming")
                #slow_down_motor
                print("slow down motor")
                (returnValue, frame_no) = od.search_animal(frame_no, True)            #cb1.cancel()

            if returnValue == -1:
                print("nicht gefunden")
                #cb1.cancel()
                #cb2.cancel()
                return False
                    
        #cb1.cancel()
        #cb2.cancel()

    #Funktion für den Greifarm
    def greifen(self):        
        t_greifer = time.time() + Consts.TIME_TO_GRAB
        print("running out gripper")
        while time.time() < t_greifer:
            i="zeit vergeht"
            #self.gripper.ausfahren([duty])

        #self.gripper.stop()
            
        #self.gripper.servomotor("down")
        print("servomotor down")

        t_greifer = time.time() + Consts.TIME_TO_GRAB
        print("running in gripper")
        while time.time() < t_greifer:
            i="zeit vergeht"
            #self.gripper.einfahren([duty])

    ###Funktion für Weiterfahren
    def weiterfahren(self):
        #wird nur gebraucht, wenn es oben deaktiviert wurde:
        #cb1 = pi.callback(18, pigpio.EITHER_EDGE, self.ir.ir_signal_changed_left)
        #cb2 = pi.callback(19, pigpio.EITHER_EDGE, self.ir.ir_signal_changed_right)
        print("initialize ir_callback")
        #motor.motor_forward([duty])
        print("drive forward")
        while True:
            ir_sensors = self.ir.irsensors()
            if ir_sensors == "both":
                print("reached target")
                self.drive_into_target()
                break

    def drive_into_target(self):               
        t_end = time.time() + 2

        print("drive forward")
        while time.time() < t_end:
            i="zeit vergeht"
            #self.motor.forward([duty])

        print("stop")
        #self.motor.motor_stop()


    def unload_animal(self):
        t_greifer = time.time() + Consts.TIME_TO_GRAB

        print("running out gripper")
        while time.time() < t_greifer:
            i="zeit vergeht"
            #self.gripper.ausfahren([duty])

        #self.gripper.stop()

    def initial_state(self):
        print("servomotor up")
        #self.gripper.servomotor("up")
        
        t_greifer = time.time() + Consts.TIME_TO_GRAB

        print("running in gripper")
        while time.time() < t_greifer:
            i="zeit vergeht"
                #self.gripper.einfahren([duty])

        #self.gripper.stop()
