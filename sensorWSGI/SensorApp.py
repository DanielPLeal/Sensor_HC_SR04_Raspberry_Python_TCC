# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

contador = 1

print "Distância de medição em processo..."

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print "Aguardando resposta do sensor..."


while (contador < 1000 ):
    arq = open("./templates/sensor.js", "w")
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
    arq.write("{\n\"id\":" + str(contador) + "\n");
    arq.write("\n\"medida\": " + str(distance) + "\n}");
    
    #arq.write("Medida " + str(contador) + " - " + str(distance) +" cm<br>")
    #arq.write("\n")
    arq.close()
    medida = distance
             
    print "",contador," - Distância do obstáculo: ",distance," cm"
    time.sleep(2)
    contador = contador + 1
    
    


GPIO.cleanup()


