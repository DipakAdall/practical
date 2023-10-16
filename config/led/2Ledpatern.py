import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

while(True):
    GPIO.output(3, True)
    print("Led 1 On")
    GPIO.output(5, True)
    print("Led 2 On")
    GPIO.output(7, False)
    print("Led 3 Off")
    GPIO.output(11, False)
    print("Led 4 Off")
    sleep(1)
    
    GPIO.output(3, False)
    print("Led 1 Off")
    GPIO.output(5, False)
    print("Led 2 Off")
    GPIO.output(7, True)
    print("Led 3 On")
    GPIO.output(11, True)
    print("Led 4 On")
    sleep(1)
