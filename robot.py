import time
#import pigpio
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

    irCallback_Left = None
    irCallback_Right = None
    
    def __init__(self):
        print("hi")
##        self.motor = Antrieb()
##        self.ir = Infrared()
##        self.pi = pigpio.pi()
##        self.gripper = Greifer()

    def anfangsfahrt(self):
        i="hallo"
        print("initialize ir_callback")
##        self.irCallback_Left = self.pi.callback(Consts.GPIO_IR_SENSOR_LEFT
##                                    ,pigpio.EITHER_EDGE
##                                    ,self.ir.ir_signal_changed_left)
##        self.irCallback_Right = self.pi.callback(Consts.GPIO_IR_SENSOR_RIGHT
##                                    ,pigpio.EITHER_EDGE
##                                    ,self.ir.ir_signal_changed_right)
        
##        self.motor.motor_forward(Consts.MOTOR_WHEELS_FREQUENCY
##                                 ,Consts.MOTOR_WHEELS_DUTYCYLCE)
        print("drive forward")
##        t_time = time.time() + 7
##        while time.time() < t_time:
##            i="zeit vergeht"
##            ir_sensors = self.ir.irsensors()
##            print(ir_sensors)
##        self.irCallback_Left.cancel()
##        self.irCallback_Right.cancel()
##        self.motor.motor_stop()

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
                #self.motor.drive_slow(True)
##                self.motor.motor_forward(Consts.MOTOR_WHEELS_FREQUENCY_SLOW
##                                         ,Consts.MOTOR_WHEELS_DUTYCYLCE_SLOW)
                print("slow down motor")
                (returnValue, frame_no) = od.search_animal(frame_no, True)            

            if returnValue == -1:
                #print("nicht gefunden")
##                self.irCallback_Left.cancel()
##                self.irCallback_Right.cancel()
##                self.motor.motor_stop()
                return#raise Exception("nicht gefunden") 
                #return False
        print("stop stop stop")
        #self.motor.drive_slow(False)
##        self.irCallback_Left.cancel()
##        self.irCallback_Right.cancel()
##        self.motor.motor_stop()

    #Funktion fuer den Greifarm
    def greifen(self):        
        t_greifer = time.time() + Consts.TIME_TO_GRAB
        print("running out gripper")
        while time.time() < t_greifer:
            i="zeit vergeht"
##            self.gripper.ausfahren(255)
            
##        self.gripper.servomotor("down")
        print("servomotor down")

        t_greifer = time.time() + Consts.TIME_TO_GRAB
        print("running in gripper")
        while time.time() < t_greifer:
            i="zeit vergeht"
##            self.gripper.einfahren(255)
        
##        self.gripper.stop()


    def stop(self):
        print("f stop")
##        self.motor.motor_stop()
##        self.gripper.stop()
        
    ###Funktion fuer Weiterfahren
    def weiterfahren(self):
        #wird nur gebraucht, wenn es oben deaktiviert wurde:
##        self.irCallback_Left = self.pi.callback(Consts.GPIO_IR_SENSOR_LEFT
##                                    ,pigpio.EITHER_EDGE
##                                    ,self.ir.ir_signal_changed_left)
##        self.irCallback_Right = self.pi.callback(Consts.GPIO_IR_SENSOR_RIGHT
##                                    ,pigpio.EITHER_EDGE
##                                    ,self.ir.ir_signal_changed_right)
        print("initialize ir_callback")
##        self.motor.motor_forward(Consts.MOTOR_WHEELS_FREQUENCY
##                                 ,Consts.MOTOR_WHEELS_DUTYCYLCE)
        
        print("drive forward")
        while True:
##            ir_sensors = self.ir.irsensors()
            print("scanned")
##            if ir_sensors == "both":
            print("reached target - drive into it")
            self.drive_into_target()
            break

    def drive_into_target(self):               
        t_end = time.time() + Consts.TIME_TO_DRIVE_INTO_TARGET

        print("drive forward")
        while time.time() < t_end:
            i="zeit vergeht"
            break
##            self.motor.motor_forward(Consts.MOTOR_WHEELS_FREQUENCY_TARGET
##                                     ,Consts.MOTOR_WHEELS_DUTYCYLCE_TARGET)

        print("stop")
##        self.irCallback_Left.cancel()
##        self.irCallback_Right.cancel()
##        self.motor.motor_stop()


    def unload_animal(self):
        t_greifer = time.time() + Consts.TIME_TO_GRAB

        print("running out gripper")
        while time.time() < t_greifer:
            i="zeit vergeht"
##            self.gripper.ausfahren(255)

##        self.gripper.stop()

    def initial_state(self):
        print("servomotor up")
##        self.gripper.servomotor("up")
        
        t_greifer = time.time() + Consts.TIME_TO_GRAB

        print("running in gripper")
        while time.time() < t_greifer:
            i="zeit vergeht"
##            self.gripper.einfahren(255)

##        self.gripper.stop()
##        self.ir.stop()
##        self.pi.stop()
##        self.motor.motor_stop()
