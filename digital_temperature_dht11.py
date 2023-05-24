# Read temperature and humidity from dht11 sensor connected to Pin 12
from machine import Pin
from time import sleep
import rp2
import dht

# Bind and set up pins
led = Pin(25, Pin.OUT)													# Onboard LED just to indicate that board works
led.value(1)
dht11 = Pin(12)															# Device connected to pin 12

# Initialize variables
sensor = dht.DHT11(dht11)												# Create Dht object

# Loop
while True:
    sensor.measure()													# Initialize measurement
    temp = sensor.temperature()											# Write measured temperature to 'temp'
    hum = sensor.humidity()												# Write measured humidity to 'hum'
    print("Temperature: {:.1f}°C   Humidity: {:.1f}% ".format(temp, hum))
    sleep(1)