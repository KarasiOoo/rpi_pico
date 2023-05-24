# Read analog value from Pin 26. There is light sensor connected.
# Results are rounded from amount of samples defined in 'num_measurements'
from machine import Pin, ADC
import time
import rp2

# Bind and set up pins
led = Pin(25, Pin.OUT)													# Onboard LED just to indicate that board works
led.value(1)
light_sensor = ADC(26)													# Sensor connected to pin 26 in ADC input mode

# Initialize variables
num_measurements = 10													# Number of measurements to average
measurements = []  														# List to store measurements

# Loop
while True:
    light_sensor_value = light_sensor.read_u16()
    light_sensor_value = (light_sensor_value / 65535) * 100
    measurements.append(light_sensor_value)  							# Add measurement to list
    if len(measurements) >= num_measurements:							# Check if enough measurements have been taken
        average = sum(measurements) / len(measurements)					# Calculate average
        print("Average light sensor value: {:.2f}".format(average))		# Display average
        measurements = []												# Reset measurements list
    time.sleep(0.05)
