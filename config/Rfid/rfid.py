import RPi.GPIO as gpio
import time
import serial

gpio.setmode(gpio.BOARD)

# Define the valid RFID card ID
valid_id = b'400034E0FF6B'  # Replace this with the valid ID of the card you want to allow access to

# Define GPIO pin numbers for LED and Buzzer
led_pin = 11  # Replace with the actual GPIO pin number for the LED
buzzer_pin = 13  # Replace with the actual GPIO pin number for the Buzzer

gpio.setup(led_pin, gpio.OUT)
gpio.setup(buzzer_pin, gpio.OUT)

def read_rfid():
    ser = serial.Serial("/dev/ttyUSB1")
    ser.baudrate = 9600
    data = ser.read(12)
    ser.close()
    return data

try:
    while True:
        print("Place the card")
        id = read_rfid()
        print(id)

        if id == valid_id:
            print("Valid access")
            gpio.output(led_pin, gpio.HIGH)  # Turn on the LED
            gpio.output(buzzer_pin, gpio.LOW)  # Turn off the Buzzer
            time.sleep(5)  # Allow access for 5 seconds
            gpio.output(led_pin, gpio.LOW)  # Turn off the LED
        else:
            print("Invalid access")
            gpio.output(led_pin, gpio.LOW)  # Turn off the LED
            gpio.output(buzzer_pin, gpio.HIGH)  # Activate the Buzzer
            time.sleep(2)  # Sound the buzzer for 2 seconds
            gpio.output(buzzer_pin, gpio.LOW)  # Turn off the Buzzer

except KeyboardInterrupt:
    gpio.cleanup()













import RPi.GPIO as gpio
import time
import serial
gpio.setmode(gpio.BOARD)
def read_rfid():
    ser = serial.Serial("/dev/ttyUSB0") #Enter the USB Port here
    ser.baudrate = 9600
    print("read..")
    data = ser.read(12)
    ser.close()
    return data
try:
    while 1:
        print("Place the Card")
        id = read_rfid()
        print(id)     
finally:
    pass

