	
import RPi.GPIO as GPIO
import time

relayInput = 17

GPIO.setmode(GPIO.BCM)


isContinue = 5
while(isContinue > 1):
    GPIO.setup(relayInput, GPIO.OUT)
    print("OFF")
    time.sleep(1)
    GPIO.cleanup()
    print("ON")
    time.sleep(1)
    isContinue -= 1
    