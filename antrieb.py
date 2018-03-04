#import pigpio
import time

class Antrieb():

  pi = None
  M1_1 = 17
  M1_2 = 27
  M1_3 = 18
#    M2_1 = [GPIO 4]
#    M2_2 = [GPIO 5]
#    M2_3 = [GPIO 6]
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

  def motor_demo(self):
    self.pi.set_PWM_frequency(M1_1, 1000000000)

    t_end = time.time() + 5

    while time.time() < t_end:
        self.pi.set_PWM_dutycycle(M1_1, 255)
        self.pi.write(M1_2, 0)
        self.pi.write(M1_3, 1)

    self.pi.set_PWM_dutycycle(M1_1, 0)
    self.pi.stop()
