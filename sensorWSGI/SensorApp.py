# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

contador = 0

print "Distância de medição em processo..."

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print "Aguardando resposta do sensor..."

arq = open("./templates/MedSensorRasp.html", "w")
while (contador < 10 ):

    
    
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)
    
    arq.write("Medida " + str(contador) + " - " + str(distance) +" cm<br>")
    arq.write("\n")

    medida = distance
             
    print "Distância do obstáculo: ",distance," cm"
    time.sleep(0.5)
    contador = contador + 1
    


arq.close()
GPIO.cleanup()


