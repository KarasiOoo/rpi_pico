# This code check if ST1081 sensor detect object in range up to 30cm.
# Sensor is changing state on 'sensor_pin'.
# '0' indicates, that obstacle is in sensor sensitive range.
# '1' means lack of objects in sensor range.
from machine import Pin
import time

led = Pin(25, Pin.OUT)													# Onboard LED just to indicate that board works
led.value(1)

sensor_pin = Pin(16, Pin.IN)											# Pin used to read state on sensor output pin.

state_flag = 0															# Variables used to indicate changed state, just to print 
previous_state = 0														# status when it changed.

######################################################################

while True:
    sensor_value = 0
    
    for i in range(100):												# Read value from sensor output 100 times
        sensor_value += sensor_pin.value()								# Sum up it into one variable
    
    if sensor_value == 0:												# Enter when all 100 results were '0',
        #print("Obstacle detected")										# what indicates object detected.
        text = "Obstacle detected"
        state_flag = 0
    elif sensor_value == 100:											# Enter when all 100 results were '1',
        #print("No obstacle")											# what indicates no object detected.
        text = "No obstacle"
        state_flag = 1
    else:																# Enter when results are mixed, that appear 
        #print("Obstacle on the edge of range")							# when object is detected on the edge of sensor range.
        text = "Obstacle on the edge of range"
        state_flag = 2
    
    if state_flag != previous_state:									# Print status only when status change
        print(text)
    
    previous_state = state_flag
    
    time.sleep_ms(200)
