# This code provides basic function to set and use 16-sign, 2-line display with hd44780 controller
# Display is configured at the moment of running code. Display is controlled using Micropython shell.
from machine import Pin
from time import sleep, sleep_us, sleep_ms

led = Pin(25, Pin.OUT)
led.value(1)

e = Pin(16, Pin.OUT)							# Enable save operation to registers
rs = Pin(15, Pin.OUT)							# Set which register will get data (command/data)
rw = Pin(14, Pin.OUT)							# Read/Write
d4 = Pin(13, Pin.OUT)							# Data lines used for communication
d5 = Pin(12, Pin.OUT)
d6 = Pin(11, Pin.OUT)
d7 = Pin(10, Pin.OUT)
rw.value(0)

# Function definition

def SetCommandReg(command_reg7, command_reg6, command_reg5, command_reg4, command_reg3, command_reg2, command_reg1, command_reg0):
    d7.init(Pin.OUT)							# Reconfigure pins to outputs
    d6.init(Pin.OUT)
    d5.init(Pin.OUT)
    d4.init(Pin.OUT)
    
    e.value(1)									# Set proper values to control pins
    rs.value(0)
    rw.value(0)
    
    d7.value(command_reg7)						# First part of command
    d6.value(command_reg6)
    d5.value(command_reg5)
    d4.value(command_reg4)
    
    e.value(0)									# Break needed for controller to prepare for second part of command
    sleep_us(1)
    e.value(1)
    
    d7.value(command_reg3)						# Second part of command
    d6.value(command_reg2)
    d5.value(command_reg1)
    d4.value(command_reg0)
    e.value(0)
    sleep_us(1)
    
    return 0


def ReadAddressCounter():
    d7.init(Pin.IN)								# Reconfigure pins to inputs, which is necessary to aquire information
    d6.init(Pin.IN)								# about cursor address
    d5.init(Pin.IN)
    d4.init(Pin.IN)
    
    rs.value(0)									# Set setup bits to reading address
    rw.value(1)
    e.value(1)
    
    busy_flag = d7.value()						# Bit which indicate if display is busy
    address_counter6 = d6.value()				# First part of cursor address
    address_counter5 = d5.value()
    address_counter4 = d4.value()
    
    e.value(0)									# Break before second part
    sleep_us(1)
    e.value(1)
    
    address_counter3 = d7.value()				# Second part of address
    address_counter2 = d6.value()
    address_counter1 = d5.value()
    address_counter0 = d4.value()
    e.value(0)
    sleep_us(1)
    
    # Assemble aquired bits to one variable
    address_counter = (address_counter6 << 6) | (address_counter5 << 5) | (address_counter4 << 4) | (address_counter3 << 3) | (address_counter2 << 2) | (address_counter1 << 1) | address_counter0
    
    return (bin(address_counter))


def SetDataReg(data_reg7, data_reg6, data_reg5, data_reg4, data_reg3, data_reg2, data_reg1, data_reg0):
    d7.init(Pin.OUT)							# Reconfigure pins to outputs
    d6.init(Pin.OUT)
    d5.init(Pin.OUT)
    d4.init(Pin.OUT)
    
    rs.value(1)									# Set proper values to control pins, to set it into display mode
    rw.value(0)
    e.value(1)
    
    d7.value(data_reg7)							# First part of command
    d6.value(data_reg6)
    d5.value(data_reg5)
    d4.value(data_reg4)
    
    e.value(0)									# Break needed for controller to prepare for second part of command
    sleep_ms(1)
    e.value(1)
    
    d7.value(data_reg3)							# Second part of command
    d6.value(data_reg2)
    d5.value(data_reg1)
    d4.value(data_reg0)
    e.value(0)
    sleep_us(1)
    
    return 0

# Configuration LCD to first place of display

SetCommandReg(0, 0, 1, 1, 1, 0, 0, 0)				# Set (according to datasheet 8-bit but in 4-bit way) display to 8-char, 2-line mode
SetCommandReg(0, 0, 0, 0, 1, 1, 1, 0)				# Turn on display and cursor
SetCommandReg(0, 0, 0, 0, 0, 0, 1, 0)				# Return display and cursor to defult position (address 0)
#SetCommandReg(0, 0, 0, 0, 0, 0, 0, 1) 				# Clear command

# Further control is done by MicroPython shell

