#!/usr/bin/env python

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
from mfrc522 import SimpleMFRC522
import time
reader = SimpleMFRC522()
x = 0
for x in range(0, 10):
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.25)
def  main():
    id, text = reader.read()
    print(id)
    print(text)
    if id ==  439430949183:
            global x
            print(text)
            if x == 1:
                    GPIO.output(17,GPIO.LOW)
                    x = 0
            else:
                    GPIO.output(17,GPIO.HIGH)
                    x = 1
    time.sleep(0.5)
while True:
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()

GPIO.cleanup()
