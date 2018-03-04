#import pigpio
from ir_signal import Ir_signal
from antrieb import Antrieb

class Infrared():

    pi = None
    motor = None
    signal_left = Ir_signal.White.value
    signal_right = Ir_signal.White.value
#    line_follow_left = [GPIO 1]
#    line_follow_right = [GPIO 2]
    demo_counter = 0

    def __init__(self):
##        self.pi = pigpio.pi()
        self.motor = Antrieb()    
    
##    self.pi.set_mode(self.line_follow_left, pigpio.INPUT)
##    self.pi.set_mode(self.line_follow_right, pigpio.INPUT)
##    self.pi.setwarnings(False)

    def irsensors(self):
        #irL = self.pi.read(self.line_follow_left)
        #irR = self.pi.read(self.line_follow_right)
        irL = 1
        irR = 1

        none = "none"
        both = "both"
        left = "left"
        right = "right"

        self.demo_counter += 1
        if self.demo_counter >= 100:
            return both

        #Wenn beide Sensoren die Linie nicht sehen
        if(irL == 1 and irR == 1):
          return none

        #Wenn das Ziel erreicht ist
        elif(irL == 0 and irR == 0):
          return both

        #Wenn nur der linke Sensor die Linie sieht  
        elif(irL == 0 and irR == 1):
          return left

        #Wenn nur der rechte Sensor die Linie sieht  
        elif(irL == 1 and irR == 0):
          return right

    def ir_signal_changed_left(self, gpio, level, tick):
        print("ir signal changed left")

        if level == Ir_signal.Black.value:
            self.signal_left = Ir_signal.Black.value
            if self.signal_right == Ir_signal.Black.value:
                print("reached target")
                #Zielfunktion ausführen ->unnötig, wenn am Ende ir gelesen wird
            else:
                print("drive to left")
                self.motor.motor_right([duty])

        elif level == Ir_signal.White.value:
            self.signal_left = Ir_signal.White.value
            print("drive forward")
            self.motor.motor_forward([duty])

    def ir_signal_changed_right(self, gpio, level, tick):
        print("ir signal changed right")

        if level == Ir_signal.Black.value:
            self.signal_right = Ir_signal.Black.value
            if self.signal_left == Ir_signal.Black.value:
                print("reached target")
                #Zielfunktion ausführen ->unnötig, wenn am Ende ir gelesen wird
            else:
                print("drive to right")
                self.motor.motor_left([duty])

        elif level == Ir_signal.White.value:
            self.signal_right= Ir_signal.White.value
            print("drive forward")
            self.motor.motor_forward([duty])

    def ir_demo():
        pi=pigpio.pi()

        pi.set_mode(18, pigpio.INPUT)

        t_end = time.time() + 20

        reflektion = 0
        kreflektion = 0

        while time.time() < t_end:

            ir = pi.read(18)

            if(ir == 1):
                print("Reflektion")
                reflektion = reflektion + 1
            elif(ir == 0):
                print("Keine Reflektion")
                kreflektion = kreflektion + 1
                
        print(reflektion)
        print(kreflektion)
