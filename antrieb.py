#import PIGPIO

class antrieb():
  
  M1_1 = [GPIO 1]
  M1_2 = [GPIO 2]
  M1_3 = [GPIO 3]

  M2_1 = [GPIO 4]
  M2_2 = [GPIO 5]
  M2_3 = [GPIO 6]

  def __init__(self):
    pi.set_mode(antrieb.M1_1, pigpio.OUTPUT)
    pi.set_mode(antrieb.M1_2, pigpio.OUTPUT)
    pi.set_mode(antrieb.M1_3, pigpio.OUTPUT)
    pi.set_mode(antrieb.M2_1, pigpio.OUTPUT)
    pi.set_mode(antrieb.M2_2, pigpio.OUTPUT)
    pi.set_mode(antrieb.M2_3, pigpio.OUTPUT)

    pi.set_PWM_frequency(antrieb.M1_1, [frequency])
    pi.set_PWM_frequency(antrieb.M2_1, [frequency])

  def motor_forward(duty):
    pi.set_PWM_dutycycle(antrieb.M1_1, duty)
    pi.write(antrieb.M1_2, 1)
    pi.write(antrieb.M1_3, 0)

    pi.set_PWM_dutycycle(antrieb.antrieb.M2_1, duty)
    pi.write(antrieb.M2_2, 1)
    pi.write(antrieb.M2_3, 0)

  def motor_backward(duty):
    pi.set_PWM_dutycycle(antrieb.M1_1, duty)
    pi.write(antrieb.M1_2, 0)
    pi.write(antrieb.M1_3, 1)

    pi.set_PWM_dutycycle(antrieb.M2_1, duty)
    pi.write(antrieb.M2_2, 0)
    pi.write(antrieb.M2_3, 1)

  def motor_stop():
    pi.set_PWM_dutycycle(antrieb.M1_1, 0)
    pi.write(antrieb.M1_2, 1)
    pi.write(antrieb.M1_3, 1)

    pi.set_PWM_dutycycle(antrieb.M2_1, 0)
    pi.write(antrieb.M2_2, 1)
    pi.write(antrieb.M2_3, 1)

  def motor_left(duty):
    pi.set_PWM_dutycycle(antrieb.M1_1, duty)
    pi.write(antrieb.M1_2, 0)
    pi.write(antrieb.M1_3, 1)

    pi.set_PWM_dutycycle(antrieb.M2_1, 0)
    pi.write(antrieb.M2_2, 0)
    pi.write(antrieb.M2_3, 0)

  def motor_right(duty):
    pi.set_PWM_dutycycle(antrieb.M1_1, 0)
    pi.write(antrieb.M1_2, 0)
    pi.write(antrieb.M1_3, 0)

    pi.set_PWM_dutycycle(antrieb.M2_1, duty)
    pi.write(antrieb.M2_2, 0)
    pi.write(antrieb.M2_3, 1)
