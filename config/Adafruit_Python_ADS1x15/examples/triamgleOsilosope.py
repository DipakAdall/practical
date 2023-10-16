import time
import matplotlib.pyplot as plt

#import numpy
from drawnow import *

# Import the ADS1x15 module.
import Adafruit_ADS1x15

# Create an ADS1115 ADC (16-bit) instance.

adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1

val = [ ]

cnt = 0

plt.ion()

# Start continuous ADC conversions on channel 0 using the previous gain value.

adc.start_adc(0, gain=GAIN)

print('Reading ADS1x15 channel 0')

#create the figure function

def makeFig():

    plt.ylim(25,175)

    plt.title('Practical 3 Osciloscope By [ 6417,6232,6424 ]')

    plt.grid(True)

    plt.ylabel('outputs')

    plt.plot(val, 'mo-', label='Channel 0')

    plt.legend(loc='lower right')

value = 50
while (True):

    # Read the last ADC conversion value and print it out.

    #value = adc.get_last_result()


    if(value > 0 or value == 50 ):
        value += 50
    if(value >= 190):
        for i in range (2) :
            value-=50



    print('Channel 0: {0}'.format(value))

    # Sleep for half a second.

    time.sleep(0.5)

    val.append(int(value))

    drawnow(makeFig)

    plt.pause(.000001)

    cnt = cnt+1

    if(cnt>50):

        val.pop(0)
