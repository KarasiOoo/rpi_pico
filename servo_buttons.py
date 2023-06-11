# Code which allow to control servo via buttons.
# 'pin_low' is connected to button, which pushed decrease PWM filling and turn servo left
# 'pin_high' is connected to button, which pushed increase PWM filling and turn servo right
from machine import Pin
import time

led = Pin(25, Pin.OUT)													# Onboard LED just to indicate that board works
led.value(1)

pin_PWM = Pin(1, Pin.OUT)												# Pin connected to servo to control it
pin_PWM.value(0)

pin_high = Pin(13, Pin.IN)												# Input pins which are connected to buttons
pin_low = Pin(11, Pin.IN)
k = 1000																# 'kilo' metric prefix
time_on = (1500) - 15													# Position set to the middle position

######################################################################

while True:
        pin_PWM.value(1)												# Send pulse
        time.sleep_us(time_on)
        pin_PWM.value(0)
        time.sleep_us((20 * k) - time_on)

        higher = pin_high.value()										# Read buttons states
        lower = pin_low.value()
        if higher == 1 and time_on <= 2600:								# Limit upper border, to avoid exceeding working range when button is pushed.
            time_on = time_on + 5
        if lower == 1 and time_on >= 300:								# Limit lowwer border, to avoid exceeding working range when button is pushed.
            time_on = time_on - 5
            
        print(time_on)
        