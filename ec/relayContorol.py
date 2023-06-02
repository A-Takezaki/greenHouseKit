	
import RPi.GPIO as GPIO
import time

relayInput = 17
led = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(relayInput, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)

isContinue = 5

while(isContinue > 1):
    GPIO.output(relayInput, True)  # アクティブローの場合は、ここをTrueに変更します
    GPIO.output(led, True)  # アクティブローの場合は、ここをTrueに変更します
    print("OFF")
    time.sleep(1)
    GPIO.output(relayInput, False)  # アクティブローの場合は、ここをFalseに変更します
    GPIO.output(led, False)  # アクティブローの場合は、ここをFalseに変更します
    print("ON") 
    time.sleep(1)
    isContinue -= 1
GPIO.cleanup()

