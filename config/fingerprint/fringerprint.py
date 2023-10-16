import time
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

led = 26
enroll = 17
delete = 18
search = 19
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
     time.sleep(2)
        print('Waiting for finger...')
        print("\nPlace Finger")
        while not f.readImage():
            pass
        f.convertImage(0x01)
        time.sleep(2)
        result = f.searchTemplate()
        positionNumber = result[0]
        if positionNumber >= 0:
            print('Template already exists at position #' + str(positionNumber))
            print("Finger already exists")
            time.sleep(2)
            return
        print('Remove finger...')
        time.sleep(2)
        print('Waiting for same finger again...')
        print("Place Finger Again")
        while not f.readImage():
            pass
        f.convertImage(0x02)
        if f.compareCharacteristics() == 0:
            print("Fingers do not match")
            time.sleep(2)
            return
        f.createTemplate()
        positionNumber = f.storeTemplate()
        print('Finger enrolled successfully!')
        print("Stored at Pos:")
        print(str(positionNumber))
        print("successfully")
        print('New template position #' + str(positionNumber))
        time.sleep(2)

    
def delete_finger():
    print("delete")
    print('Place your finger on the sensor to delete a fingerprint...')
        gpio.output(led3, HIGH)
        while not f.readImage():
            pass
        f.convertImage(0x01)
        positionNumber = f.searchTemplate()[0]
        if positionNumber < 0:
            print('No matching fingerprint found!')
        else:
            f.deleteTemplate(positionNumber)
            print(fingerprint at position {positionNumber} deleted.')
        gpio.output(led3, LOW)

def search_finger():
    print("search")
    print('Searching for finger...')
        time.sleep(2)
        while not f.readImage():
            pass
        f.convertImage(0x01)
        time.sleep(2)
        result = f.searchTemplate()
        positionNumber = result[0]
        accuracyScore = result[1]
        if positionNumber == -1:
            print('No match found!')
            time.sleep(2)
            return
        else:
            print('Found template at position #' + str(positionNumber))
            print("Found at Pos:")
            print(str(positionNumber))
            gpio.output(led2, HIGH)
            time.sleep(2)
            gpio.output(led2, LOW)


    
while 1:
    gpio.output(led, HIGH)
    if(gpio.input(enroll) == 0):
        enroll_finger()
    if(gpio.input(delete) == 0):
        delete_finger()
    if(gpio.input(search) == 0):
        search_finger()

except KeyboardInterrupt:
    gpio.cleanup()
import time
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

led = 26
enroll = 17
delete = 18
search = 19
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
     time.sleep(2)
        print('Waiting for finger...')
        print("\nPlace Finger")
        while not f.readImage():
            pass
        f.convertImage(0x01)
        time.sleep(2)
        result = f.searchTemplate()
        positionNumber = result[0]
        if positionNumber >= 0:
            print('Template already exists at position #' + str(positionNumber))
            print("Finger already exists")
            time.sleep(2)
            return
        print('Remove finger...')
        time.sleep(2)
        print('Waiting for same finger again...')
        print("Place Finger Again")
        while not f.readImage():
            pass
        f.convertImage(0x02)
        if f.compareCharacteristics() == 0:
            print("Fingers do not match")
            time.sleep(2)
            return
        f.createTemplate()
        positionNumber = f.storeTemplate()
        print('Finger enrolled successfully!')
        print("Stored at Pos:")
        print(str(positionNumber))
        print("successfully")
        print('New template position #' + str(positionNumber))
        time.sleep(2)

    
def delete_finger():
    print("delete")
    print('Place your finger on the sensor to delete a fingerprint...')
        gpio.output(led3, HIGH)
        while not f.readImage():
            pass
        f.convertImage(0x01)
        positionNumber = f.searchTemplate()[0]
        if positionNumber < 0:
            print('No matching fingerprint found!')
        else:
            f.deleteTemplate(positionNumber)
            print(fingerprint at position {positionNumber} deleted.')
        gpio.output(led3, LOW)

def search_finger():
    print("search")
    print('Searching for finger...')
        time.sleep(2)
        while not f.readImage():
            pass
        f.convertImage(0x01)
        time.sleep(2)
        result = f.searchTemplate()
        positionNumber = result[0]
        accuracyScore = result[1]
        if positionNumber == -1:
            print('No match found!')
            time.sleep(2)
            return
        else:
            print('Found template at position #' + str(positionNumber))
            print("Found at Pos:")
            print(str(positionNumber))
            gpio.output(led2, HIGH)
            time.sleep(2)
            gpio.output(led2, LOW)


    
while 1:
    gpio.output(led, HIGH)
    if(gpio.input(enroll) == 0):
        enroll_finger()
    if(gpio.input(delete) == 0):
        delete_finger()
    if(gpio.input(search) == 0):
        search_finger()

except KeyboardInterrupt:
    gpio.cleanup()
import time
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

led = 26
enroll = 17
delete = 18
search = 19
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
     time.sleep(2)
        print('Waiting for finger...')
        print("\nPlace Finger")
        while not f.readImage():
            pass
        f.convertImage(0x01)
        time.sleep(2)
        result = f.searchTemplate()
        positionNumber = result[0]
        if positionNumber >= 0:
            print('Template already exists at position #' + str(positionNumber))
            print("Finger already exists")
            time.sleep(2)
            return
        print('Remove finger...')
        time.sleep(2)
        print('Waiting for same finger again...')
        print("Place Finger Again")
        while not f.readImage():
            pass
        f.convertImage(0x02)
        if f.compareCharacteristics() == 0:
            print("Fingers do not match")
            time.sleep(2)
            return
        f.createTemplate()
        positionNumber = f.storeTemplate()
        print('Finger enrolled successfully!')
        print("Stored at Pos:")
        print(str(positionNumber))
        print("successfully")
        print('New template position #' + str(positionNumber))
        time.sleep(2)

    
def delete_finger():
    print("delete")
    print('Place your finger on the sensor to delete a fingerprint...')
        gpio.output(led3, HIGH)
        while not f.readImage():
            pass
        f.convertImage(0x01)
        positionNumber = f.searchTemplate()[0]
        if positionNumber < 0:
            print('No matching fingerprint found!')
        else:
            f.deleteTemplate(positionNumber)
            print(fingerprint at position {positionNumber} deleted.')
        gpio.output(led3, LOW)

def search_finger():
    print("search")
    print('Searching for finger...')
        time.sleep(2)
        while not f.readImage():
            pass
        f.convertImage(0x01)
        time.sleep(2)
        result = f.searchTemplate()
        positionNumber = result[0]
        accuracyScore = result[1]
        if positionNumber == -1:
            print('No match found!')
            time.sleep(2)
            return
        else:
            print('Found template at position #' + str(positionNumber))
            print("Found at Pos:")
            print(str(positionNumber))
            gpio.output(led2, HIGH)
            time.sleep(2)
            gpio.output(led2, LOW)


    
while 1:
    gpio.output(led, HIGH)
    if(gpio.input(enroll) == 0):
        enroll_finger()
    if(gpio.input(delete) == 0):
        delete_finger()
    if(gpio.input(search) == 0):
        search_finger()

except KeyboardInterrupt:
    gpio.cleanup()
import time
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

led = 26
enroll = 17
delete = 18
search = 19
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
     time.sleep(2)
        print('Waiting for finger...')
        print("\nPlace Finger")
        while not f.readImage():
            pass
        f.convertImage(0x01)
        time.sleep(2)
        result = f.searchTemplate()
        positionNumber = result[0]
        if positionNumber >= 0:
            print('Template already exists at position #' + str(positionNumber))
            print("Finger already exists")
            time.sleep(2)
            return
        print('Remove finger...')
        time.sleep(2)
        print('Waiting for same finger again...')
        print("Place Finger Again")
        while not f.readImage():
            pass
        f.convertImage(0x02)
        if f.compareCharacteristics() == 0:
            print("Fingers do not match")
            time.sleep(2)
            return
        f.createTemplate()
        positionNumber = f.storeTemplate()
        print('Finger enrolled successfully!')
        print("Stored at Pos:")
        print(str(positionNumber))
        print("successfully")
        print('New template position #' + str(positionNumber))
        time.sleep(2)

    
def delete_finger():
    print("delete")
    print('Place your finger on the sensor to delete a fingerprint...')
        gpio.output(led3, HIGH)
        while not f.readImage():
            pass
        f.convertImage(0x01)
        positionNumber = f.searchTemplate()[0]
        if positionNumber < 0:
            print('No matching fingerprint found!')
        else:
            f.deleteTemplate(positionNumber)
            print(fingerprint at position {positionNumber} deleted.')
        gpio.output(led3, LOW)

def search_finger():
    print("search")
    print('Searching for finger...')
        time.sleep(2)
        while not f.readImage():
            pass
        f.convertImage(0x01)
        time.sleep(2)
        result = f.searchTemplate()
        positionNumber = result[0]
        accuracyScore = result[1]
        if positionNumber == -1:
            print('No match found!')
            time.sleep(2)
            return
        else:
            print('Found template at position #' + str(positionNumber))
            print("Found at Pos:")
            print(str(positionNumber))
            gpio.output(led2, HIGH)
            time.sleep(2)
            gpio.output(led2, LOW)


    
while 1:
    gpio.output(led, HIGH)
    if(gpio.input(enroll) == 0):
        enroll_finger()
    if(gpio.input(delete) == 0):
        delete_finger()
    if(gpio.input(search) == 0):
        search_finger()

except KeyboardInterrupt:
    gpio.cleanup()
import time
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

led = 26
enroll = 17
delete = 18
search = 19
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
     time.sleep(2)
        print('Waiting for finger...')
        print("\nPlace Finger")
        while not f.readImage():
            pass
        f.convertImage(0x01)
        time.sleep(2)
        result = f.searchTemplate()
        positionNumber = result[0]
        if positionNumber >= 0:
            print('Template already exists at position #' + str(positionNumber))
            print("Finger already exists")
            time.sleep(2)
            return
        print('Remove finger...')
        time.sleep(2)
        print('Waiting for same finger again...')
        print("Place Finger Again")
        while not f.readImage():
            pass
        f.convertImage(0x02)
        if f.compareCharacteristics() == 0:
            print("Fingers do not match")
            time.sleep(2)
            return
        f.createTemplate()
        positionNumber = f.storeTemplate()
        print('Finger enrolled successfully!')
        print("Stored at Pos:")
        print(str(positionNumber))
        print("successfully")
        print('New template position #' + str(positionNumber))
        time.sleep(2)

    
def delete_finger():
    print("delete")
    print('Place your finger on the sensor to delete a fingerprint...')
        gpio.output(led3, HIGH)
        while not f.readImage():
            pass
        f.convertImage(0x01)
        positionNumber = f.searchTemplate()[0]
        if positionNumber < 0:
            print('No matching fingerprint found!')
        else:
            f.deleteTemplate(positionNumber)
            print(fingerprint at position {positionNumber} deleted.')
        gpio.output(led3, LOW)

def search_finger():
    print("search")
    print('Searching for finger...')
        time.sleep(2)
        while not f.readImage():
            pass
        f.convertImage(0x01)
        time.sleep(2)
        result = f.searchTemplate()
        positionNumber = result[0]
        accuracyScore = result[1]
        if positionNumber == -1:
            print('No match found!')
            time.sleep(2)
            return
        else:
            print('Found template at position #' + str(positionNumber))
            print("Found at Pos:")
            print(str(positionNumber))
            gpio.output(led2, HIGH)
            time.sleep(2)
            gpio.output(led2, LOW)


    
while 1:
    gpio.output(led, HIGH)
    if(gpio.input(enroll) == 0):
        enroll_finger()
    if(gpio.input(delete) == 0):
        delete_finger()
    if(gpio.input(search) == 0):
        search_finger()

except KeyboardInterrupt:
    gpio.cleanup()
import time
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

led = 26
enroll = 17
delete = 18
search = 19
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
     time.sleep(2)
        print('Waiting for finger...')
        print("\nPlace Finger")
        while not f.readImage():
            pass
        f.convertImage(0x01)
        time.sleep(2)
        result = f.searchTemplate()
        positionNumber = result[0]
        if positionNumber >= 0:
            print('Template already exists at position #' + str(positionNumber))
            print("Finger already exists")
            time.sleep(2)
            return
        print('Remove finger...')
        time.sleep(2)
        print('Waiting for same finger again...')
        print("Place Finger Again")
        while not f.readImage():
            pass
        f.convertImage(0x02)
        if f.compareCharacteristics() == 0:
            print("Fingers do not match")
            time.sleep(2)
            return
        f.createTemplate()
        positionNumber = f.storeTemplate()
        print('Finger enrolled successfully!')
        print("Stored at Pos:")
        print(str(positionNumber))
        print("successfully")
        print('New template position #' + str(positionNumber))
        time.sleep(2)

    
def delete_finger():
    print("delete")
    print('Place your finger on the sensor to delete a fingerprint...')
        gpio.output(led3, HIGH)
        while not f.readImage():
            pass
        f.convertImage(0x01)
        positionNumber = f.searchTemplate()[0]
        if positionNumber < 0:
            print('No matching fingerprint found!')
        else:
            f.deleteTemplate(positionNumber)
            print(fingerprint at position {positionNumber} deleted.')
        gpio.output(led3, LOW)

def search_finger():
    print("search")
    print('Searching for finger...')
        time.sleep(2)
        while not f.readImage():
            pass
        f.convertImage(0x01)
        time.sleep(2)
        result = f.searchTemplate()
        positionNumber = result[0]
        accuracyScore = result[1]
        if positionNumber == -1:
            print('No match found!')
            time.sleep(2)
            return
        else:
            print('Found template at position #' + str(positionNumber))
            print("Found at Pos:")
            print(str(positionNumber))
            gpio.output(led2, HIGH)
            time.sleep(2)
            gpio.output(led2, LOW)


    
while 1:
    gpio.output(led, HIGH)
    if(gpio.input(enroll) == 0):
        enroll_finger()
    if(gpio.input(delete) == 0):
        delete_finger()
    if(gpio.input(search) == 0):
        search_finger()

except KeyboardInterrupt:
    gpio.cleanup()
import time
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

led = 26
enroll = 17
delete = 18
search = 19
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
     time.sleep(2)
        print('Waiting for finger...')
        print("\nPlace Finger")
        while not f.readImage():
            pass
        f.convertImage(0x01)
        time.sleep(2)
        result = f.searchTemplate()
        positionNumber = result[0]
        if positionNumber >= 0:
            print('Template already exists at position #' + str(positionNumber))
            print("Finger already exists")
            time.sleep(2)
            return
        print('Remove finger...')
        time.sleep(2)
        print('Waiting for same finger again...')
        print("Place Finger Again")
        while not f.readImage():
            pass
        f.convertImage(0x02)
        if f.compareCharacteristics() == 0:
            print("Fingers do not match")
            time.sleep(2)
            return
        f.createTemplate()
        positionNumber = f.storeTemplate()
        print('Finger enrolled successfully!')
        print("Stored at Pos:")
        print(str(positionNumber))
        print("successfully")
        print('New template position #' + str(positionNumber))
        time.sleep(2)

    
def delete_finger():
    print("delete")
    print('Place your finger on the sensor to delete a fingerprint...')
        gpio.output(led3, HIGH)
        while not f.readImage():
            pass
        f.convertImage(0x01)
        positionNumber = f.searchTemplate()[0]
        if positionNumber < 0:
            print('No matching fingerprint found!')
        else:
            f.deleteTemplate(positionNumber)
            print(fingerprint at position {positionNumber} deleted.')
        gpio.output(led3, LOW)

def search_finger():
    print("search")
    print('Searching for finger...')
        time.sleep(2)
        while not f.readImage():
            pass
        f.convertImage(0x01)
        time.sleep(2)
        result = f.searchTemplate()
        positionNumber = result[0]
        accuracyScore = result[1]
        if positionNumber == -1:
            print('No match found!')
            time.sleep(2)
            return
        else:
            print('Found template at position #' + str(positionNumber))
            print("Found at Pos:")
            print(str(positionNumber))
            gpio.output(led2, HIGH)
            time.sleep(2)
            gpio.output(led2, LOW)


    
while 1:
    gpio.output(led, HIGH)
    if(gpio.input(enroll) == 0):
        enroll_finger()
    if(gpio.input(delete) == 0):
        delete_finger()
    if(gpio.input(search) == 0):
        search_finger()

except KeyboardInterrupt:
    gpio.cleanup()
import time
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

led = 26
enroll = 17
delete = 18
search = 19
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
     time.sleep(2)
        print('Waiting for finger...')
        print("\nPlace Finger")
        while not f.readImage():
            pass
        f.convertImage(0x01)
        time.sleep(2)
        result = f.searchTemplate()
        positionNumber = result[0]
        if positionNumber >= 0:
            print('Template already exists at position #' + str(positionNumber))
            print("Finger already exists")
            time.sleep(2)
            return
        print('Remove finger...')
        time.sleep(2)
        print('Waiting for same finger again...')
        print("Place Finger Again")
        while not f.readImage():
            pass
        f.convertImage(0x02)
        if f.compareCharacteristics() == 0:
            print("Fingers do not match")
            time.sleep(2)
            return
        f.createTemplate()
        positionNumber = f.storeTemplate()
        print('Finger enrolled successfully!')
        print("Stored at Pos:")
        print(str(positionNumber))
        print("successfully")
        print('New template position #' + str(positionNumber))
        time.sleep(2)

    
def delete_finger():
    print("delete")
    print('Place your finger on the sensor to delete a fingerprint...')
        gpio.output(led3, HIGH)
        while not f.readImage():
            pass
        f.convertImage(0x01)
        positionNumber = f.searchTemplate()[0]
        if positionNumber < 0:
            print('No matching fingerprint found!')
        else:
            f.deleteTemplate(positionNumber)
            print(fingerprint at position {positionNumber} deleted.')
        gpio.output(led3, LOW)

def search_finger():
    print("search")
    print('Searching for finger...')
        time.sleep(2)
        while not f.readImage():
            pass
        f.convertImage(0x01)
        time.sleep(2)
        result = f.searchTemplate()
        positionNumber = result[0]
        accuracyScore = result[1]
        if positionNumber == -1:
            print('No match found!')
            time.sleep(2)
            return
        else:
            print('Found template at position #' + str(positionNumber))
            print("Found at Pos:")
            print(str(positionNumber))
            gpio.output(led2, HIGH)
            time.sleep(2)
            gpio.output(led2, LOW)


    
while 1:
    gpio.output(led, HIGH)
    if(gpio.input(enroll) == 0):
        enroll_finger()
    if(gpio.input(delete) == 0):
        delete_finger()
    if(gpio.input(search) == 0):
        search_finger()

except KeyboardInterrupt:
    gpio.cleanup()
