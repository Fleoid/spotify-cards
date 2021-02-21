#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

reader = SimpleMFRC522()

GPIO.setup(17,GPIO.OUT)
def  main():
        id, text = reader.read()
        print(id)
        print(text)
        if text ==  "Whoope":
                x = 0
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
