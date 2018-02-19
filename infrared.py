class infrared():
  
  line_follow_left = [GPIO 1]
  line_follow_right = [GPIO 2]

  def __init__(self):
    pi.set_mode(line_follow_left, pigpio.INPUT)
    pi.set_mode(line_follow_right, pigpio.INPUT)
    pi.setwarnings(False)

  def irsensors():
    irL = pi.read(line_follow_left)
    irR = pi.read(line_follow_right)

    none = "none"
    both = "both"
    left = "left"
    right = "right"

    #Wenn beide Sensoren die Linie nicht sehen
    if(irL == 1 and irR == 1)
      return none

    #Wenn das Ziel erreicht ist
    elif(irL == 0 and irR == 0)
      return both

    #Wenn nur der linke Sensor die Linie sieht  
    elif(irL == 0 and irR == 1)
      return left

    #Wenn nur der rechte Sensor die Linie sieht  
    elif(irL == 1 and irR == 0)
      return right


  #Später in anderer Funktion
  while True:
    infrared_sensors = infrared.irsensors()

    if(infrared_sensors == "none")
      antrieb.motor_forward([frequency])

    elif(infrared_sensors == "both")
      antrieb.motor_forward([frequency])
      t = Timer([Sekunden], antrieb.stop())
      t.start()
      #Auslade-Prozess starten

    elif(infrared_sensors == "left")
      antrieb.motor_right([frequency])

    elif(infrared_sensors == "right")
      antrieb.motor_left([frequency])
