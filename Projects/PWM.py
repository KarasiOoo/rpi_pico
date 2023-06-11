# Simple code to learn how use PWM on RPi Pico with Micropython.
# LED connected to digital_pin will be controlled via PWM
from machine import Pin
import time

led = Pin(25, Pin.OUT)													# Onboard LED just to indicate that board works
led.value(1)

pin_led = Pin(1, Pin.OUT)												# LED which will be controlled via PWM
pin_led.value(0)

time_on = 1015															# Amount of filling, in range (0-1023)

######################################################################

while True:
    pin_led.value(1)													# PWM in loop
    time.sleep_ms(time_on)
    pin_led.value(0)
    time.sleep_ms(1023 - time_on)
