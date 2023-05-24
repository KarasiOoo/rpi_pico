# Turn on first and last led of WS2812 array. Just to check the length of array.
import rp2
import neopixel
from machine import Pin
from time import sleep_ms

# Bind and set up pins
led = Pin(25, Pin.OUT)													# Onboard LED just to indicate that board works
led.value(1)
control_pin = Pin(26)

# Initialize variables
num_leds = 8															# Amount of WS2812 leds in array
ws2812 = neopixel.NeoPixel(control_pin, num_leds)						# Initialize NeoPixel object

# Loop
if True:
    ws2812[0] = (20, 0, 20)												# Set pink to first led
    ws2812[7] = (0, 5, 0)												# Set green to last led
    ws2812.write()														# Send config to leds
