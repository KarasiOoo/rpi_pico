#this programm is blinking 3 leds

from machine import Pin
import time
import rp2

#bind and set up pins
led = Pin(25, Pin.OUT)
led_green = Pin(4, Pin.OUT)
led_yellow = Pin(3, Pin.OUT)
led_red = Pin(2, Pin.OUT)

#set entry values
led.value(1)
led_green.value(0)
led_yellow.value(0)
led_red.value(0)

#switching lighting leds
while True:
    led_green.value(0)
    led_red.value(1)
    time.sleep(0.5)
    led_red.value(0)
    led_yellow.value(1)
    time.sleep(0.5)
    led_yellow.value(0)
    led_green.value(1)
    time.sleep(0.5)