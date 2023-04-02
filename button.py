#This programm is changing lighting led by pressing button

from machine import Pin
import time
import rp2

#bind and set up pins
led = Pin(25, Pin.OUT)
led_green = Pin(4, Pin.OUT)
led_yellow = Pin(3, Pin.OUT)
led_red = Pin(2, Pin.OUT)
button = Pin(0, Pin.IN)

#set values for the beggining
status = 0										#variable which consists state 
led.value(1)
led_green.value(0)
led_yellow.value(0)
led_red.value(0)

#loop 
while True:
    button_value = button.value()				#check state on input
    if button_value != 0:						#go in if button is pushed
        if status == 0:
            led_green.value(0)					#turn off leds
            led_yellow.value(0)
            led_red.value(1)					#turn on specific led
            print("Red")						#print name of lighting led in shell
        elif status == 1:
            led_green.value(0)
            led_yellow.value(1)
            led_red.value(0)
            print("Yellow")
        elif status == 2:
            led_green.value(1)
            led_yellow.value(0)
            led_red.value(0)
            print("Green")
            
        status = status + 1
        
    if status > 2:								#reset variable after exceed expected range
        status = 0
    
    time.sleep(0.15)							#delay used to avoid reading multiple times one button push