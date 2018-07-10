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
    line_follow_left = 22
    line_follow_right = 24
    demo_counter = 0

    def __init__(self):
        self.pi = pigpio.pi()
        self.motor = Antrieb()    
    
        self.pi.set_mode(self.line_follow_left, pigpio.INPUT)
        self.pi.set_mode(self.line_follow_right, pigpio.INPUT)
##    self.pi.setwarnings(False)

    def irsensors(self):
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
                    self.motor.motor_right(10000, 750000)

            elif level == Ir_signal.White.value:
                self.signal_left = Ir_signal.White.value
                print("drive forward")
                self.motor.motor_forward(10000, 750000)
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
                    self.motor.motor_left(10000, 750000)

            elif level == Ir_signal.White.value:
                self.signal_right= Ir_signal.White.value
                print("drive forward")
                self.motor.motor_forward(10000, 750000)
            old_tick_right = tick
            print(tick)

    def stop():
        self.pi.stop()
 
