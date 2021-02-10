#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

reader = SimpleMFRC522()


def  main():
        id, text = reader.read()
        print(id)
        print(text)
        time.sleep(0.5)
while True:
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()

GPIO.cleanup()