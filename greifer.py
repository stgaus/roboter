import pigpio as pi
import time

class greifer():

  def __init__(self):
    M3_1 = [GPIO 1]
    M3_2 = [GPIO 2]
    M3_3 = [GPIO 3]

    servo = [GPIO 4]
    
    pi.set_mode(M3_1, pigpio.OUTPUT)
    pi.set_mode(M3_2, pigpio.OUTPUT)
    pi.set_mode(M3_3, pigpio.OUTPUT)

    pi.set_mode(servo, pigpio.OUTPUT)

    pi.set_PWM_frequency(M3_1, [frequency])

  def ausfahren(duty):
    pi.set_PWM_dutycycle(self.M3_1, duty)
    pi.write(self.M3_2, 1)
    pi.write(self.M3_3, 0)

  def einfahren(duty):
    pi.set_PWM_dutycycle(self.M3_1, duty)
    pi.write(self.M3_2, 1)
    pi.write(self.M3_3, 0)

  def stop():
    pi.set_PWM_dutycycle(self.M3_1, 0)
    pi.write(self.M3_2, 1)
    pi.write(self.M3_3, 1)

  def servomotor(position):
    p = pi.set_PWM_frequency(self.servo, 50)
    t_end = time.time() + 3

    if position == "up"
      while time.time() < t_end:
        p.set_PWM_dutycycle(self.servo, 12,5)
        time.sleep(1)
        p.stop()
     elif position == "down"
        p.set_PWM_dutycycle(self.servo, 2,5)
        time.sleep(1)
        p.stop()
