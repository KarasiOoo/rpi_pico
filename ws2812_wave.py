# Light "running" led on ws2812 8-led array, change color after each iteration
import rp2
import neopixel
from machine import Pin
from time import sleep

# Bind and set up pins
led = Pin(25, Pin.OUT)													# Onboard LED just to indicate that board works
led.value(1)
control_pin = Pin(26)

# Initialize variables
num_leds = 8															# Amount of WS2812 leds in array
power = 8																# Power of leds (range 0-255)
ws2812 = neopixel.NeoPixel(control_pin, num_leds)						# Initialize NeoPixel object
rgb_values = [(power, 0, 0), (power, power, 0), (0, power, 0), (0, power, power), (0, 0, power), (power, 0, power)]
# List contains prepared colours
j = 0																	# Variable used to go through 'rgb_value' list

# Loop
while True:
    for i in range(num_leds):											# Loop which is going through each led in array
        ws2812.fill((0, 0, 0))											# Turn off all leds
        ws2812[i] = rgb_values[j]										# Set colour from list to one led from array
        ws2812.write()													# Send prepared config to leds
        """																# "
        j+= 1															# Code block which switch each next led with next colour
        if j >= len(rgb_values):
            j = 0
        """																# "
        sleep(0.1)
                                                                        # ""
    j+= 1																# Code block which switch colour after going through whole array
    if j >= len(rgb_values):
            j = 0
                                                                        # ""

