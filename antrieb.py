#import pigpio
import time

class Antrieb():

  pi = None
  M1_1 = 18
  M1_2 = 17
  M1_3 = 27
  
  M2_1 = 19
  M2_2 = 16
  M2_3 = 26
  frequency = 0

  def __init__(self):
    pass
##    self.pi = pigpio.pi()
##    
##    self.pi.set_mode(self.M1_1, pigpio.OUTPUT)
##    self.pi.set_mode(self.M1_2, pigpio.OUTPUT)
##    self.pi.set_mode(self.M1_3, pigpio.OUTPUT)
##    self.pi.set_mode(self.M2_1, pigpio.OUTPUT)
##    self.pi.set_mode(self.M2_2, pigpio.OUTPUT)
##    self.pi.set_mode(self.M2_3, pigpio.OUTPUT)
##
##    self.pi.set_PWM_frequency(self.M1_1, self.frequency)
##    self.pi.set_PWM_frequency(self.M2_1, self.frequency)

  def motor_forward(self, duty):
    self.pi.set_PWM_dutycycle(self.M1_1, duty)
    self.pi.write(self.M1_2, 1)
    self.pi.write(self.M1_3, 0)

    self.pi.set_PWM_dutycycle(self.M2_1, duty)
    self.pi.write(self.M2_2, 1)
    self.pi.write(self.M2_3, 0)

  def motor_backward(self, duty):
    self.pi.set_PWM_dutycycle(self.M1_1, duty)
    self.pi.write(self.M1_2, 0)
    self.pi.write(self.M1_3, 1)

    self.pi.set_PWM_dutycycle(self.M2_1, duty)
    self.pi.write(self.M2_2, 0)
    self.pi.write(self.M2_3, 1)

  def motor_stop(self):
    self.pi.set_PWM_dutycycle(self.M1_1, 0)
    self.pi.write(self.M1_2, 1)
    self.pi.write(self.M1_3, 1)

    self.pi.set_PWM_dutycycle(self.M2_1, 0)
    self.pi.write(self.M2_2, 1)
    self.pi.write(self.M2_3, 1)

    self.pi.stop()

  def motor_left(self, duty):
    self.pi.set_PWM_dutycycle(self.M1_1, duty)
    self.pi.write(self.M1_2, 1)
    self.pi.write(self.M1_3, 0)

    self.pi.set_PWM_dutycycle(self.M2_1, 0)
    self.pi.write(self.M2_2, 0)
    self.pi.write(self.M2_3, 0)

  def motor_right(duty):
    self.pi.set_PWM_dutycycle(self.M1_1, 0)
    self.pi.write(self.M1_2, 0)
    self.pi.write(self.M1_3, 0)

    self.pi.set_PWM_dutycycle(self.M2_1, duty)
    self.pi.write(self.M2_2, 1)
    self.pi.write(self.M2_3, 0)
