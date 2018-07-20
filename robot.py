import time
#import pigpio
from antrieb import Antrieb
from infrared import Infrared
from greifer import Greifer
from consts import Consts
from objectDetection import ObjectDetection
from imutils.video import VideoStream

class Robot():

    motor = None
    ir = None
    gripper = None
    pi = None
    camera = None

    irCallback_Left = None
    irCallback_Right = None
    
    def __init__(self):
        pass
        # self.motor = Antrieb()
        # self.ir = Infrared()
        # self.pi = pigpio.pi()
        # self.gripper = Greifer()
        
##    Funktion fuer die Anfangsfahrt
    def anfangsfahrt(self):
        # self.irCallback_Left = self.pi.callback(Consts.GPIO_IR_SENSOR_LEFT
        #                             ,pigpio.EITHER_EDGE
        #                             ,self.ir.ir_signal_changed_left)
        # self.irCallback_Right = self.pi.callback(Consts.GPIO_IR_SENSOR_RIGHT
        #                             ,pigpio.EITHER_EDGE
        #                             ,self.ir.ir_signal_changed_right)
        print("initialize ir_callback")
        # self.motor.motor_forward(Consts.MOTOR_WHEELS_FREQUENCY
        #                          ,Consts.MOTOR_WHEELS_DUTYCYLCE)
        print("drive forward")

    def looking_for_animal(self, animalType):
        found_animal = False
        #scannt fuer Tier
        od = ObjectDetection(animalType)
        self.camera = VideoStream(0, False, (640, 480))
        (found_animal, frame_no) = od.search_animal(0, False, self.motor, self.camera, self)
            
        #stoppt Motor, wenn Tier gefunden wird
        if found_animal == True:
            print("i found " + animalType.name)
            # self.irCallback_Left.cancel()
            # self.irCallback_Right.cancel()
            # print("stop stop stop")
            # self.motor.motor_stop()

        elif found_animal == False:
            print("animal not found")
            return False
        #self.camera.stop()
        return True

    #Funktion fuer den Greifarm
    def greifen(self):        
        t_greifer = time.time() + Consts.TIME_TO_GRAB
        print("running out gripper")
        while time.time() < t_greifer:
            i="zeit vergeht"
            #self.gripper.ausfahren(255)
            
        #self.gripper.servomotor("down")
        print("servomotor down")

        t_greifer = time.time() + Consts.TIME_TO_GRAB
        print("running in gripper")
        while time.time() < t_greifer:
            i="zeit vergeht"
            #self.gripper.einfahren(255)
        
        #self.gripper.stop()


    def stop(self):
        print("stop")
        self.motor.motor_stop()
        self.camera.stop()
        self.gripper.stop()
        
    ###Funktion fuer Weiterfahren
    def weiterfahren(self):
        #wird nur gebraucht, wenn es oben deaktiviert wurde:
        self.irCallback_Left = self.pi.callback(Consts.GPIO_IR_SENSOR_LEFT
                                    ,pigpio.EITHER_EDGE
                                    ,self.ir.ir_signal_changed_left)
        self.irCallback_Right = self.pi.callback(Consts.GPIO_IR_SENSOR_RIGHT
                                    ,pigpio.EITHER_EDGE
                                    ,self.ir.ir_signal_changed_right)
        print("initialize ir_callback")
        self.motor.motor_forward(Consts.MOTOR_WHEELS_FREQUENCY_END
                                 ,Consts.MOTOR_WHEELS_DUTYCYLCE_END)
        
        print("drive forward")
        while True:
            ir_sensors = self.ir.irsensors()
            #print("scanned", " ", ir_sensors)
            if ir_sensors == "both":
                print("reached target - drive into it")
                self.drive_into_target()
                break

    def drive_into_target(self):               
        t_end = time.time() + Consts.TIME_TO_DRIVE_INTO_TARGET

        print("drive forward")
        while time.time() < t_end:
            i="zeit vergeht"
            self.motor.motor_forward(Consts.MOTOR_WHEELS_FREQUENCY_TARGET
                                     ,Consts.MOTOR_WHEELS_DUTYCYLCE_TARGET)

        print("stop")
        self.irCallback_Left.cancel()
        self.irCallback_Right.cancel()
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
        #self.ir.stop()        
        self.motor.motor_stop()
        self.pi.stop()
