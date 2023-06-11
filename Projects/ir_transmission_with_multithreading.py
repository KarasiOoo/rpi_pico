## Ir transmission with multithreading, transmitting triggered by button, recieveing indicated by LED
import rp2
from machine import Pin
from time import sleep_ms
import _thread

# Bind and set up pins
led = Pin(25, Pin.OUT)													# Onboard LED just to indicate that board works
led.value(1)
button = Pin(0, Pin.IN)													# Input to detect button push
ir_receiver = Pin(1, Pin.IN)											# Input of IR receiver
signal_indicating_led = Pin(2, Pin.OUT)									# LED which indicates recieving IR signal
ir_led = Pin(22, Pin.OUT)												# IR led/transmitter

# Define function which will be done by core0
def core0_thread():
    while True:
        button_value = button.value()
        if button_value != 0:
            ir_led.value(1)
        else:
            ir_led.value(0)
        sleep_ms(1)
 
# Define function which will be done by core1 
def core1_thread():
    while True:
        ir_receiver_value = ir_receiver.value()
        if ir_receiver_value != 1:
            signal_indicating_led.value(1)
        else:
            signal_indicating_led.value(0)
        sleep_ms(1)
 
# Starts new (second) thread and assign function which will be done by second core
second_thread = _thread.start_new_thread(core1_thread, ())

# Initialize function/thread, which will be done by first core 
core0_thread()

# Please note, the order of threads/core_code must be as above, core1 first, core0 second