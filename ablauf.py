#Tier eingeben
#Kamera und Infrarot-Sensoren starten
#Antrieb starten
#Wenn der Roboter vom Weg abkommt, sollen sich die Infrarot-Sensoren melden, dass sie die schwarze Linie sehen
#Wenn links die schwarze Linie sieht, muss nur rechts angetrieben werden
#Wenn rechts die schwarze Linie sieht, muss nur links angetrieben werden
#Wenn die Kamera das gesuchte Tier sieht, muss der Roboter sich so ausrichten, dass sich das Tier in der Mitte der Kamera befindet
#So wird sichergestellt, dass der Greifmechanismus das Tier greifen kann
#Anschließend wird der Greifmechanismus ausgefahren werden
#Schieber umklappen, der sich dann hinter dem Tier im Regal befindet
#Mechanismus wieder einfahren und das Tier mit dem Schieber auf eine am Roboter angebrachte Plattform schieben
#Antrieb wieder starten, gemeinsam mit den Infrator-Sensoren
#Fahren bis beide Infrarot-Sensoren die schwarze Linie gleichzeitig sehen --> Ziel erreicht
#Anschließend noch ein bisschen weiterfahren (Entweder über Sekunden oder wenn die schwarze Linie wieder gesehen wird)
#Greifmechanismus wieder ausfahren und mit einem zweiten Schieber das Tier von der Plattform schieben

##############################

#Funktion für die Anfangsfahrt
def anfangsfahrt():
	while True:
		#scannt für Tier
		#beendet Schleife, wenn Tier gefunden wird
		#Funktion für Greifen ausführen

		ir = infrared.irsensors()

		if(ir == "none")
			motor_forward([duty])
			
		elif(ir == "left")
			motor_right([duty])
			
		elif(ir == "right")
			motor_left([duty])

##############################

#Funktion für den Greifarm
def greifen():
	t_greifer = time.time() + [Zeit]

	while time.time() < t_greifer():
		greifer.ausfahren([duty])

	greifer.stop()
	
	greifer.servomotor("down")

	while time.time() < t_greifer():
		greifer.einfahren([duty])
		
	greifer.stop()

#Anschließend Funktion für Weiterfahren ausführen

##############################

#Funktion für Weiterfahren
def weiterfahren():
	while True:
		
		ir = infrared.irsensors()

		if(ir == "none")
			motor_forward([duty])
			
		elif(ir == "left")
			motor_right([duty])

		elif(ir == "right")
			motor_left([duty])

		elif(ir == "both")
			t_end = time.time() + [Zeit]
			
			while time.time() < t_end:
				motor.forward([duty])

			motor_stop()
			
			t_greifer = time.time() + [Zeit]
			
			while time.time() < t_greifer:
				greifer.ausfahren([duty])
			
			greifer.stop()
			
			greifer.servomotor("up")
			
			while time.time() < t_greifer:
				greifer.einfahren([duty])
			
			greifer.stop()
