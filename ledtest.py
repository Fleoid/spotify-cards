import Rpi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

GPIO.output(4,GPIO.HIGH)
time.sleep(1)
GPIO.output(4,GPIO.LOW)
GPIO.output(17,GPIO.HIGH)
time.sleep(1)
GPIO.output(17,GPIO.LOW)
GPIO.output(22,GPIO.HIGH)
time.sleep(1)
GPIO.output(22,GPIO.LOW)




GPIO.output(4,GPIO.HIGH)
GPIO.output(17,GPIO.HIGH)
time.sleep(1)
GPIO.output(17,GPIO.LOW)
GPIO.output(4,GPIO.LOW)

GPIO.output(17,GPIO.HIGH)
GPIO.output(22,GPIO.HIGH)
time.sleep(1)
GPIO.output(17,GPIO.LOW)
GPIO.output(22,GPIO.LOW)

GPIO.output(4,GPIO.HIGH)
GPIO.output(22,GPIO.HIGH)
time.sleep(1)
GPIO.output(4,GPIO.LOW)
GPIO.output(22,GPIO.LOW)

GPIO.output(17,GPIO.HIGH)
GPIO.output(22,GPIO.HIGH)
sleep(1)
GPIO.output(17,GPIO.LOW)
GPIO.output(22,GPIO.LOW)
GPIO.cleanup()
exit()
