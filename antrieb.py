#import pigpio
import time
from consts import Consts

class Antrieb():

  pi = None
  M1_1 = 18
  M1_2 = 17
  M1_3 = 27
  
  M2_1 = 19
  M2_2 = 16
  M2_3 = 26

  drive_slow = False
  
  def __init__(self):
    self.pi = pigpio.pi()

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


  def drive_slow(self, boolean):
    self.drive_slow1 = boolean

  def setEnd(self, boolean):
    self.drive_end = boolean
  
  def motor_forward(self, frequency, duty):
    if self.pi is None or not self.pi.connected:
      self.pi = pigpio.pi()
    if self.drive_slow1 == True:
      self.pi.hardware_PWM(self.M1_1, Consts.MOTOR_WHEELS_FREQUENCY_SLOW, Consts.MOTOR_WHEELS_DUTYCYLCE_SLOW)
    #self.pi.set_PWM_dutycycle(self.M1_1, duty)
    elif self.drive_end == True:
        self.pi.hardware_PWM(self.M1_1, Consts.MOTOR_WHEELS_FREQUENCY_END, Consts.MOTOR_WHEELS_DUTYCYLCE_END)
    else:
      self.pi.hardware_PWM(self.M1_1, frequency, duty)
    self.pi.write(self.M1_2, 0)
    self.pi.write(self.M1_3, 1)

    if self.drive_slow1 == True:
      self.pi.hardware_PWM(self.M2_1, Consts.MOTOR_WHEELS_FREQUENCY_SLOW, Consts.MOTOR_WHEELS_DUTYCYLCE_SLOW)
    #self.pi.set_PWM_dutycycle(self.M2_1, duty)
    else:
      self.pi.hardware_PWM(self.M2_1, frequency, duty)
    self.pi.write(self.M2_2, 0)
    self.pi.write(self.M2_3, 1)

  def motor_backward(self, frequency, duty):
    if self.pi is None or not self.pi.connected:
      self.pi = pigpio.pi()
    if self.drive_slow1 == True:
      self.pi.hardware_PWM(self.M1_1, Consts.MOTOR_WHEELS_FREQUENCY_SLOW, Consts.MOTOR_WHEELS_DUTYCYLCE_SLOW)
    #self.pi.set_PWM_dutycycle(self.M1_1, duty)
    elif self.drive_end == True:
      self.pi.hardware_PWM(self.M1_1, Consts.MOTOR_WHEELS_FREQUENCY_END, Consts.MOTOR_WHEELS_DUTYCYLCE_END)
    else:
      self.pi.hardware_PWM(self.M1_1, frequency, duty)
    self.pi.write(self.M1_2, 1)
    self.pi.write(self.M1_3, 0)

    if self.drive_slow1 == True:
      self.pi.hardware_PWM(self.M2_1, Consts.MOTOR_WHEELS_FREQUENCY_SLOW, Consts.MOTOR_WHEELS_DUTYCYLCE_SLOW)
    #self.pi.set_PWM_dutycycle(self.M2_1, duty)
    else:
      self.pi.hardware_PWM(self.M2_1, frequency, duty)
    self.pi.write(self.M2_2, 1)
    self.pi.write(self.M2_3, 0)

  def motor_stop(self):
    if self.pi is None or not self.pi.connected:
      self.pi = pigpio.pi()
    self.pi.set_PWM_dutycycle(self.M1_1, 0)
    self.pi.hardware_PWM(self.M1_1, 0, 0)
    self.pi.write(self.M1_2, 1)
    self.pi.write(self.M1_3, 1)

    self.pi.set_PWM_dutycycle(self.M2_1, 0)
    self.pi.hardware_PWM(self.M1_1, 0, 0)
    self.pi.write(self.M2_2, 1)
    self.pi.write(self.M2_3, 1)

    self.pi.stop()

  def motor_right(self, frequency, duty):
    if self.pi is None or not self.pi.connected:
      self.pi = pigpio.pi()
    if self.drive_slow1 == True:
      self.pi.hardware_PWM(self.M1_1, Consts.MOTOR_WHEELS_FREQUENCY_SLOW, Consts.MOTOR_WHEELS_DUTYCYLCE_SLOW)
    #self.pi.set_PWM_dutycycle(self.M1_1, duty)
    elif self.drive_end == True:
      self.pi.hardware_PWM(self.M1_1, Consts.MOTOR_WHEELS_FREQUENCY_END, Consts.MOTOR_WHEELS_DUTYCYLCE_END)
    else:
      self.pi.hardware_PWM(self.M1_1, frequency, duty)
    self.pi.write(self.M1_2, 0)
    self.pi.write(self.M1_3, 1)

    self.pi.set_PWM_dutycycle(self.M2_1, 0)
    #self.pi.hardware_PWM(self.M1_1, Consts.MOTOR_WHEELS_FREQUENCY_SLOW, Consts.MOTOR_WHEELS_DUTYCYLCE_SLOW)
    self.pi.write(self.M2_2, 0)
    self.pi.write(self.M2_3, 0)

  def motor_left(self, frequency, duty):
    if self.pi is None or not self.pi.connected:
      self.pi = pigpio.pi()
    self.pi.set_PWM_dutycycle(self.M1_1, 0)
    #self.pi.hardware_PWM(self.M1_1, Consts.MOTOR_WHEELS_FREQUENCY_SLOW, Consts.MOTOR_WHEELS_DUTYCYLCE_SLOW)
    self.pi.write(self.M1_2, 0)
    self.pi.write(self.M1_3, 0)

    if self.drive_slow1 == True:
      self.pi.hardware_PWM(self.M2_1, Consts.MOTOR_WHEELS_FREQUENCY_SLOW, Consts.MOTOR_WHEELS_DUTYCYLCE_SLOW)
    elif self.drive_end == True:
      self.pi.hardware_PWM(self.M1_1, Consts.MOTOR_WHEELS_FREQUENCY_END, Consts.MOTOR_WHEELS_DUTYCYLCE_END)
    #self.pi.set_PWM_dutycycle(self.M2_1, duty)
    else:
      self.pi.hardware_PWM(self.M2_1, frequency, duty)
    self.pi.write(self.M2_2, 0)
    self.pi.write(self.M2_3, 1)

