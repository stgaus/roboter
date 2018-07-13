import pigpio
import time
from ir_signal import Ir_signal
from antrieb import Antrieb
from consts import Consts

class Infrared():

    pi = None
    motor = None
    signal_left = Ir_signal.White.value
    signal_right = Ir_signal.White.value
    old_tick_right = 0
    old_tick_left = 0
    line_follow_left = Consts.GPIO_IR_SENSOR_LEFT
    line_follow_right = Consts.GPIO_IR_SENSOR_RIGHT
    demo_counter = 0

    def __init__(self):
        self.pi = pigpio.pi()
        self.motor = Antrieb()    
    
        self.pi.set_mode(self.line_follow_left, pigpio.INPUT)
        self.pi.set_mode(self.line_follow_right, pigpio.INPUT)
##    self.pi.setwarnings(False)

    def irsensors(self):
        if self.pi is None or not self.pi.connected:
          self.pi = pigpio.pi()
        irL = self.pi.read(self.line_follow_left)
        irR = self.pi.read(self.line_follow_right)

        none = "none"
        both = "both"
        left = "left"
        right = "right"

        #Wenn beide Sensoren die Linie nicht sehen
        if(irL == Ir_signal.White.value and irR == Ir_signal.White.value):
          return none

        #Wenn das Ziel erreicht ist
        elif(irL == Ir_signal.Black.value and irR == Ir_signal.Black.value):
          return both

        #Wenn nur der linke Sensor die Linie sieht  
        elif(irL == Ir_signal.Black.value and irR == Ir_signal.White.value):
          return left

        #Wenn nur der rechte Sensor die Linie sieht  
        elif(irL == Ir_signal.White.value and irR == Ir_signal.Black.value):
          return right

    def ir_signal_changed_left(self, gpio, level, tick):
        print("ir signal changed left")
        if (self.old_tick_left + Consts.TIME_TO_LAST_IR_TICK) < tick:
            if level == Ir_signal.Black.value:
                self.signal_left = Ir_signal.Black.value
                if self.signal_right == Ir_signal.Black.value:
                    print("callback reached target")
                else:
                    print("drive to left")
##                    self.motor.motor_stop()
##                    t_time = time.time() + 0.4
##                    while time.time() < t_time:
##                        i="zeit vergeht"
                    self.motor.motor_right(Consts.MOTOR_WHEELS_FREQUENCY_STEER
                                           ,Consts.MOTOR_WHEELS_DUTYCYLCE_STEER)

            elif level == Ir_signal.White.value:
                self.signal_left = Ir_signal.White.value
                print("drive forward")
##                self.motor.motor_stop()
##                t_time = time.time() + 0.4
##                while time.time() < t_time:
##                    i="zeit vergeht"
                self.motor.motor_forward(Consts.MOTOR_WHEELS_FREQUENCY
                                         ,Consts.MOTOR_WHEELS_DUTYCYLCE)
            old_tick_left = tick            

    def ir_signal_changed_right(self, gpio, level, tick):
        print("ir signal changed right")
        if (self.old_tick_right + Consts.TIME_TO_LAST_IR_TICK) < tick:
            if level == Ir_signal.Black.value:
                self.signal_right = Ir_signal.Black.value
                if self.signal_left == Ir_signal.Black.value:
                    print("callback reached target")
                else:
                    print("drive to right")
##                    self.motor.motor_stop()
##                    t_time = time.time() + 0.4
##                    while time.time() < t_time:
##                        i="zeit vergeht"
                    self.motor.motor_left(Consts.MOTOR_WHEELS_FREQUENCY_STEER
                                          ,Consts.MOTOR_WHEELS_DUTYCYLCE_STEER)

            elif level == Ir_signal.White.value:
                self.signal_right= Ir_signal.White.value
                print("drive forward")
##                self.motor.motor_stop()
##                t_time = time.time() + 0.4
##                while time.time() < t_time:
##                    i="zeit vergeht"
                self.motor.motor_forward(Consts.MOTOR_WHEELS_FREQUENCY
                                         ,Consts.MOTOR_WHEELS_DUTYCYLCE)
            old_tick_right = tick
            print(tick)

    def stop():
        self.pi.stop()
 
