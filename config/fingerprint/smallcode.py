import time
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

led = 26
enroll = 29
delete = 31
search = 35
HIGH = 1
LOW = 0

gpio.setup(led, gpio.OUT)
gpio.setup(enroll, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(delete, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(search, gpio.IN, pull_up_down = gpio.PUD_UP)

try:
    f = PyFingerprint("/dev/ttyUSB0", 57600, 0xFFFFFFFF, 0x00000000)
    print("Fingerprint scanner ready")
except Exception as e:
    print("Exception message : " + str(e))

def enroll_finger():
    print("enroll")
    
def delete_finger():
    print("delete")
    
def search_finger():
    print("search")
    
while 1:
    gpio.output(led, HIGH)
    if(gpio.input(enroll) == 0):
        enroll_finger()
    if(gpio.input(delete) == 0):
        delete_finger()
    if(gpio.input(search) == 0):
        search_finger()

