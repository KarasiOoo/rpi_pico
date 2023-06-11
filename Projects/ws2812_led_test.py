# Code perform test of every led in each ws2812 RGBled. Its turn on each color led in every led-module
# and switch to next every one second
import machine
import neopixel
import time

led = machine.Pin(25, machine.Pin.OUT)									# Onboard LED just to indicate that board works
led.value(1)

# Define the number of LEDs and the pin used to control the WS2812 strip
num_leds = 8
pin = machine.Pin(2)

# Initialize the neopixel object
strip = neopixel.NeoPixel(pin, num_leds)

# Define variables
power = 10
switch_time = 1000

# Define some colors to display on the LEDs
red = (power, 0, 0)
green = (0, power, 0)
blue = (0, 0, power)

# Loop through the colors and display them on the LEDs
while True:
    strip.fill(red)
    strip.write()
    time.sleep_ms(switch_time)
    strip.fill(green)
    strip.write()
    time.sleep_ms(switch_time)
    strip.fill(blue)
    strip.write()
    time.sleep_ms(switch_time)
