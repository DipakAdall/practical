import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT,initial=GPIO.LOW)
While True:    
    GPIO.output(7,GPIO.HIGH)
    print("LED on")    
    sleep(1)          
    GPIO.output(7,GPIO.LOW)    
    print("LED off")    
    sleep(1)
