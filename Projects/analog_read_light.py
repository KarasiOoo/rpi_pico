#Reading analog value from photoresistor
from machine import Pin, ADC
import time
import rp2

#Bind and set up pins
led = Pin(25, Pin.OUT)
led.value(1)
light_sensor = ADC(26)

#Loop
while True:
    light_sensor_value = light_sensor.read_u16()						#read voltage from analog input in uint16
    light_sensor_value = (light_sensor_value / 65535) * 100				#convert binary value into 0-100 scale
    print("{:.2f}".format(light_sensor_value))
    time.sleep(1)
