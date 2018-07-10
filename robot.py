import time
import pigpio
from antrieb import Antrieb
from infrared import Infrared
from greifer import Greifer
from consts import Consts
from objectDetection1 import ObjectDetection

class Robot():

    motor = None
    ir = None
    gripper = None
    pi = None

    cb1 = None
    cb2 = None
    
    def __init__(self):
        self.motor = Antrieb()
        self.ir = Infrared()
        self.pi = pigpio.pi()
        self.gripper = Greifer()
        
##    Funktion fuer die Anfangsfahrt
    def anfangsfahrt(self):
        self.cb1 = self.pi.callback(22, pigpio.EITHER_EDGE, self.ir.ir_signal_changed_left)
        self.cb2 = self.pi.callback(24, pigpio.EITHER_EDGE, self.ir.ir_signal_changed_right)
        print("initialize ir_callback")
        self.motor.motor_forward(10000, 750000)
        print("drive forward")
        #t_time = time.time() + 10
        #while time.time() < t_time:
        #    i="zeit vergeht"
        #    ir_sensors = self.ir.irsensors()
        #    #print(ir_sensors)
        #self.cb1.cancel()
        #self.cb2.cancel()
        #self.motor.motor_stop()

    def looking_for_animal(self, animalType):
        returnValue = 0
        while True:
            #scannt fuer Tier
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
                self.motor.motor_forward(1000, 300000)
                print("slow down motor")
                (returnValue, frame_no) = od.search_animal(frame_no, True)            

            if returnValue == -1:
                print("nicht gefunden")
                self.cb1.cancel()
                self.cb2.cancel()
                self.motor.motor_stop()
                return False
        print("stop stop stop")           
        self.cb1.cancel()
        self.cb2.cancel()
        self.motor.motor_stop()

    #Funktion fuer den Greifarm
    def greifen(self):        
        t_greifer = time.time() + Consts.TIME_TO_GRAB
        print("running out gripper")
        while time.time() < t_greifer:
            i="zeit vergeht"
            self.gripper.ausfahren(255)
            
        self.gripper.servomotor("down")
        print("servomotor down")

        t_greifer = time.time() + Consts.TIME_TO_GRAB
        print("running in gripper")
        while time.time() < t_greifer:
            i="zeit vergeht"
            self.gripper.einfahren(255)
        
        self.gripper.stop()


    def stop(self):
        self.motor.motor_stop()
        self.gripper.stop()
        
    ###Funktion fuer Weiterfahren
    def weiterfahren(self):
        #wird nur gebraucht, wenn es oben deaktiviert wurde:
        self.cb1 = self.pi.callback(22, pigpio.EITHER_EDGE, self.ir.ir_signal_changed_left)
        self.cb2 = self.pi.callback(24, pigpio.EITHER_EDGE, self.ir.ir_signal_changed_right)
        print("initialize ir_callback")
        self.motor.motor_forward(10000, 750000)
        print("drive forward")
        while True:
            ir_sensors = self.ir.irsensors()
            #print("scanned", " ", ir_sensors)
            if ir_sensors == "both":
                print("reached target - drive into it")
                self.drive_into_target()
                break

    def drive_into_target(self):               
        t_end = time.time() + 3

        print("drive forward")
        while time.time() < t_end:
            i="zeit vergeht"
            self.motor.motor_forward(4000, 500000)

        print("stop")
        self.cb1.cancel()
        self.cb2.cancel()
        self.motor.motor_stop()


    def unload_animal(self):
        t_greifer = time.time() + Consts.TIME_TO_GRAB

        print("running out gripper")
        while time.time() < t_greifer:
            i="zeit vergeht"
            self.gripper.ausfahren(255)

        self.gripper.stop()

    def initial_state(self):
        print("servomotor up")
        self.gripper.servomotor("up")
        
        t_greifer = time.time() + Consts.TIME_TO_GRAB

        print("running in gripper")
        while time.time() < t_greifer:
            i="zeit vergeht"
            self.gripper.einfahren(255)

        self.gripper.stop()
        self.ir.stop()
        self.pi.stop()
        self.motor.motor_stop()
