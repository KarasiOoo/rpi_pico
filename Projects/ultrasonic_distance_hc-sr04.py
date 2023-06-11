# This code is reading distance from HC-SR04 sensor.
# It sends impuls in 'trigger_pin' which sends ultrasonic wave.
# Then it continously read state on 'echo_pin' waiting for state change into '1' which indicates beginning of 'echo' signal
# and waiting for next state change into '0' which means finish of 'echo' signal.
# Delta time divided by 58 gives distance in centimeters.
# Nextly makes rounding from amount of recorded samples stored in 'samples'.
from machine import Pin
import time

led = Pin(25, Pin.OUT)													# Onboard LED just to indicate that board works
led.value(1)

trigger_pin = Pin(17, Pin.OUT)											# Pin used to send trigger signal to sensor
echo_pin = Pin(16, Pin.IN)												# Pin which is used to read echo signal from sensor

samples = 50															# Amount of samples used to rounding
distance_full = 0														# Variable used to sum up all results before rounding
# echo = 0																# TODO: Test if this replacement would work

######################################################################

while True:
    distance_full = 0
    for i in range(samples):											# Loop which perform measurement and sum up results in 'distance_full'
        trigger_pin.value(1)											# Trigger signal
        time.sleep_us(20)
        trigger_pin.value(0)
        
        echo = echo_pin.value()											# TODO: Remove and check if basic declaration works
        while echo == 0:												# Loop which stuck until state '1' on 'echo_pin' (rising_edge)
            echo = echo_pin.value()
        
        start = time.ticks_us()											# Read 'rising_egde' time
        
        echo = echo_pin.value()											# TODO: Check if removing that affect working
        while echo == 1:												# Loop which stuck until state '0' on 'echo_pin' (falling_edge)
            echo = echo_pin.value()
            
        stop = time.ticks_us()											# Read 'falling_egde' time
        
        distance = (stop - start) / 58									# Calculate distance

        distance_full += distance										# Sum up distance
        time.sleep_ms(10)
        
    distance_avg = distance_full / samples								# Round results
    if distance_avg > 500:												# Print "Out of range" because sensor reads up to 500
        print("Out of range")
    else:
        print(distance_avg)
    #time.sleep(1)
