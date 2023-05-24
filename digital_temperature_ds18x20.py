# Read temperature from digital temperature sensor ds18x20 connected to Pin 13.
from machine import Pin
import rp2, time
import onewire, ds18x20

# Bind and set up pins
led = Pin(25, Pin.OUT)									# Onboard LED just to indicate that board works
led.value(1)
ds18 = Pin(13)											# Device connected to pin 13

# Initialize variables
sensor = onewire.OneWire(ds18)							# Create Onewire object
digital_temp = ds18x20.DS18X20(sensor)					# and specify target type

roms = digital_temp.scan()								# Scan for devices on the bus

# Loop
while True:    
    digital_temp.convert_temp()							# Initialize measurement
    time.sleep(1)										# Delay for process measurement (at least 750ms)
    for rom in roms:									# Go through all devices connected to onewire bus
        print("Temperature:{:.4f}" .format(digital_temp.read_temp(rom))) # Read temperature from each device
