#import pigpio 
import time

class Greifer():

##  M3_1 = [GPIO 1]
##  M3_2 = [GPIO 2]
##  M3_3 = [GPIO 3]

##  servo = [GPIO 4]
  pi = None

  def __init__(self):
    pass
    #pi = pigpio.pi()
    
##    self.pi.set_mode(self.M3_1, pigpio.OUTPUT)
##    self.pi.set_mode(self.M3_2, pigpio.OUTPUT)
##    self.pi.set_mode(self.M3_3, pigpio.OUTPUT)
##
##    self.pi.set_mode(self.servo, pigpio.OUTPUT)
##
##    self.pi.set_PWM_frequency(self.M3_1, [frequency])

  def ausfahren(self, duty):
    self.pi.set_PWM_dutycycle(self.M3_1, duty)
    self.pi.write(self.M3_2, 1)
    self.pi.write(self.M3_3, 0)

  def einfahren(self, duty):
    self.pi.set_PWM_dutycycle(self.M3_1, duty)
    self.pi.write(self.M3_2, 1)
    self.pi.write(self.M3_3, 0)

  def stop(self):
    self.pi.set_PWM_dutycycle(self.M3_1, 0)
    self.pi.write(self.M3_2, 1)
    self.pi.write(self.M3_3, 1)

  def servomotor(self, position):
    t_end = time.time() + 3

    if position == "up":
      while time.time() < t_end:
        self.pi.set_servo_pulsewidth(self.servo, 1500)
        time.sleep(1)
        self.pi.stop()
    elif position == "down":
      self.pi.set_servo_pulsewidth(self.servo, 1000)
      time.sleep(1)
      self.pi.stop()
