# Ir transmission, transmitting triggered by button, recieveing indicated by LED
import rp2
from machine import Pin
from time import sleep_ms

# Bind and set up pins
led = Pin(25, Pin.OUT)										# Onboard LED just to indicate that board works
led.value(1)
button = Pin(0, Pin.IN)
ir_receiver = Pin(1, Pin.IN)
signal_indicating_led = Pin(2, Pin.OUT)
ir_led = Pin(22, Pin.OUT)

# Loop
while True:
    button_value = button.value()							# Read button state
    if button_value != 0:									# If button pressed, turn on IR-led.
        ir_led.value(1)
    else:
        ir_led.value(0)
    
    ir_receiver_value = ir_receiver.value()					# Read IR-receiver 
    if ir_receiver_value != 1:
        signal_indicating_led.value(1)						# LED = !IR-receiver, due to IR-receiver characeristic.
    else:													# It gives LOW on output when got signal.
        signal_indicating_led.value(0)
    
    sleep_ms(1)
    

