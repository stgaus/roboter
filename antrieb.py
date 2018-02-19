#import PIGPIO

class antrieb():

  def __init__(self):
    M1_1 = [GPIO 1]
    M1_2 = [GPIO 2]
    M1_3 = [GPIO 3]

    M2_1 = [GPIO 4]
    M2_2 = [GPIO 5]
    M2_3 = [GPIO 6]
    
    pi.set_mode(M1_1, pigpio.OUTPUT)
    pi.set_mode(M1_2, pigpio.OUTPUT)
    pi.set_mode(M1_3, pigpio.OUTPUT)
    pi.set_mode(M2_1, pigpio.OUTPUT)
    pi.set_mode(M2_2, pigpio.OUTPUT)
    pi.set_mode(M2_3, pigpio.OUTPUT)

    pi.set_PWM_frequency(M1_1, [frequency])
    pi.set_PWM_frequency(M2_1, [frequency])

  def motor_forward(duty):
    pi.set_PWM_dutycycle(self.M1_1, duty)
    pi.write(self.M1_2, 1)
    pi.write(self.M1_3, 0)

    pi.set_PWM_dutycycle(self.M2_1, duty)
    pi.write(self.M2_2, 1)
    pi.write(self.M2_3, 0)

  def motor_backward(duty):
    pi.set_PWM_dutycycle(self.M1_1, duty)
    pi.write(self.M1_2, 0)
    pi.write(self.M1_3, 1)

    pi.set_PWM_dutycycle(self.M2_1, duty)
    pi.write(self.M2_2, 0)
    pi.write(self.M2_3, 1)

  def motor_stop():
    pi.set_PWM_dutycycle(self.M1_1, 0)
    pi.write(self.M1_2, 1)
    pi.write(self.M1_3, 1)

    pi.set_PWM_dutycycle(self.M2_1, 0)
    pi.write(self.M2_2, 1)
    pi.write(self.M2_3, 1)

  def motor_left(duty):
    pi.set_PWM_dutycycle(self.M1_1, duty)
    pi.write(self.M1_2, 1)
    pi.write(self.M1_3, 0)

    pi.set_PWM_dutycycle(self.M2_1, 0)
    pi.write(self.M2_2, 0)
    pi.write(self.M2_3, 0)

  def motor_right(duty):
    pi.set_PWM_dutycycle(self.M1_1, 0)
    pi.write(self.M1_2, 0)
    pi.write(self.M1_3, 0)

    pi.set_PWM_dutycycle(self.M2_1, duty)
    pi.write(self.M2_2, 1)
    pi.write(self.M2_3, 0)
