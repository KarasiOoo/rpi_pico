# This code provides basic function to set and use 16-sign, 2-line display with hd44780 controller
# Display is configured at the moment of running code. Display is controlled using Micropython shell.
from machine import Pin
from time import sleep, sleep_us, sleep_ms

set_mode = 0b00111000
turn_on_display = 0b00001110
home = 0b00000010
clear = 0b00000001

chars = {
    ' ': 0b00100000, '0': 0b00110000, '1': 0b00110001, '2': 0b00110010,
    '3': 0b00110011, '4': 0b00110100, '5': 0b00110101, '6': 0b00110110,
    '7': 0b00110111, '8': 0b00111000, '9': 0b00111001, 'A': 0b01000001,
    'B': 0b01000010, 'C': 0b01000011, 'D': 0b01000100, 'E': 0b01000101,
    'F': 0b01000110, 'G': 0b01000111, 'H': 0b01001000, 'I': 0b01001001,
    'J': 0b01001010, 'K': 0b01001011, 'L': 0b01001100, 'M': 0b01001101,
    'N': 0b01001110, 'O': 0b01001111, 'P': 0b01010000, 'Q': 0b01010001,
    'R': 0b01010010, 'S': 0b01010011, 'T': 0b01010100, 'U': 0b01010101,
    'V': 0b01010110, 'W': 0b01010111, 'X': 0b01011000, 'Y': 0b01011011,
    'Z': 0b01011010, 'a': 0b01100001, 'b': 0b01100010, 'c': 0b01100011,
    'd': 0b01100100, 'e': 0b01100101, 'f': 0b01100110, 'g': 0b01100111,
    'h': 0b01101000, 'i': 0b01101001, 'j': 0b01101010, 'k': 0b01101011,
    'l': 0b01101100, 'm': 0b01101101, 'n': 0b01101110, 'o': 0b01101111,
    'p': 0b01110000, 'q': 0b01110001, 'r': 0b01110010, 's': 0b01110011,
    't': 0b01110100, 'u': 0b01110101, 'v': 0b01110110, 'w': 0b01110111,
    'x': 0b01111000, 'y': 0b01111001, 'z': 0b01111010, '.': 0b00101110,
    ',': 0b00101100, '!': 0b00100001, '(': 0b00101000, ')': 0b00101001,
    '%': 0b00100101, '*': 0b00101010, '+': 0b00101011, '-': 0b00101101,
    '=': 0b00111101, '?': 0b00111111, '/': 0b00101111, '<': 0b00111100,
    '>': 0b00111110, '[': 0b01011011, ']': 0b01011101, '_': 0b01011111
}


led = Pin(25, Pin.OUT)
led.value(1)

e = Pin(2, Pin.OUT)									# Enable save operation to registers
rs = Pin(0, Pin.OUT)								# Set which register will get data (command/data)
rw = Pin(1, Pin.OUT)								# Read/Write
d4 = Pin(17, Pin.OUT)								# Data lines used for communication
d5 = Pin(16, Pin.OUT)
d6 = Pin(14, Pin.OUT)
d7 = Pin(15, Pin.OUT)
rw.value(0)

# Function definition

# Function which writes 'command_reg' value into command register, which is used to configure display.
def SetCommandReg(command_reg):
    d7.init(Pin.OUT)								# Reconfigure pins to outputs
    d6.init(Pin.OUT)
    d5.init(Pin.OUT)
    d4.init(Pin.OUT)
    
    e.value(1)										# Set proper values to control pins
    rs.value(0)
    rw.value(0)
    
    d7.value((command_reg >> 7) & 0b1)				# First part of command
    d6.value((command_reg >> 6) & 0b1)
    d5.value((command_reg >> 5) & 0b1)
    d4.value((command_reg >> 4) & 0b1)
    
    e.value(0)										# Break needed for controller to prepare for second part of command
    sleep_us(1)
    e.value(1)
    
    d7.value((command_reg >> 3) & 0b1)				# Second part of command
    d6.value((command_reg >> 2) & 0b1)
    d5.value((command_reg >> 1) & 0b1)
    d4.value(command_reg & 0b1)
    e.value(0)
    sleep_us(1)
    
    return 0


# Function which read busy flag and cursor address.
def ReadAddressCounter():
    d7.init(Pin.IN)									# Reconfigure pins to inputs, which is necessary to aquire information
    d6.init(Pin.IN)									# about cursor address
    d5.init(Pin.IN)
    d4.init(Pin.IN)
    
    rs.value(0)										# Set setup bits to reading address
    rw.value(1)
    e.value(1)
    
    busy_flag = d7.value()							# Bit which indicate if display is busy
    address_counter6 = d6.value()					# First part of cursor address
    address_counter5 = d5.value()
    address_counter4 = d4.value()
    
    e.value(0)										# Break before second part
    sleep_us(1)	
    e.value(1)
    
    address_counter3 = d7.value()					# Second part of address
    address_counter2 = d6.value()
    address_counter1 = d5.value()
    address_counter0 = d4.value()
    e.value(0)
    sleep_us(1)
    
    # Assemble aquired bits to one variable
    address_counter = (address_counter6 << 6) | (address_counter5 << 5) | (address_counter4 << 4) | (address_counter3 << 3) | (address_counter2 << 2) | (address_counter1 << 1) | address_counter0
    
    return (bin(address_counter))


# Function which writes 'data_reg' value into data register, which cause display coresponding char on display.
def SetDataReg(data_reg):
    d7.init(Pin.OUT)								# Reconfigure pins to outputs
    d6.init(Pin.OUT)
    d5.init(Pin.OUT)
    d4.init(Pin.OUT)
    
    rs.value(1)										# Set proper values to control pins, to set it into display mode
    rw.value(0)
    e.value(1)
    
    d7.value((data_reg >> 7) & 0b1)					# First part of command
    d6.value((data_reg >> 6) & 0b1)
    d5.value((data_reg >> 5) & 0b1)
    d4.value((data_reg >> 4) & 0b1)
    
    e.value(0)										# Break needed for controller to prepare for second part of command
    sleep_ms(1)
    e.value(1)
    
    d7.value((data_reg >> 3) & 0b1)					# Second part of command
    d6.value((data_reg >> 2) & 0b1)
    d5.value((data_reg >> 1) & 0b1)
    d4.value(data_reg & 0b1)
    e.value(0)
    sleep_us(1)
    
    return 0



####################################################

# Configuration LCD to first place of display

SetCommandReg(set_mode)								# Set (according to datasheet 8-bit but in 4-bit way) display to 8-char, 2-line mode
SetCommandReg(turn_on_display)						# Turn on display and cursor
SetCommandReg(home)									# Return display and cursor to defult position (address 0)
SetCommandReg(clear) 								# Clear command

# Further control is done by MicroPython shell

while True:
    print("What to do?")
    print("1 - Write a string to display it on display.")
    print("2 - Show cursor address.")
    print("3 - Clear display.")
    print("4 - Change address of cursor.\n ")
    
    choice = str(input("Choose from above menu: "))
    
    if choice == "1":
        print("Write an array: ")
        text = input()
        for x in text:
            if x == "|":
                SetCommandReg(0b11000000)
            else:
                SetDataReg(chars[x])
                cursor_address = int(ReadAddressCounter())
                if cursor_address > 15 and cursor_address <= 63:
                    #cursor_address = 0b11000000
                    SetCommandReg(0b11000000)
                elif cursor_address > 80 and cursor_address <= 127:
                    #cursor_address = 0b10000000
                    SetCommandReg(0b10000000)
                sleep_us(100)
        
    elif choice == "2":
        read_cursor_address = ReadAddressCounter()
        print("Cursor is set to: bin = " + bin(read_cursor_address) + "\n\n")# + ", int = " + int(read_cursor_address))
        sleep_ms(1000)
        
    elif choice == "3":
        print("Clearing...")
        sleep_ms(300)
        clear_error = SetCommandReg(clear)
        if clear_error == 0:
            print("Clearing done!\n\n")
        else:
            print("Error occur while clearing display!\n\n")
        
    elif choice == "4":
        new_address = int(input("Enter an address where you want to jump: "))
        new_address += 128
        new_address = new_address
        #print(new_address)
        SetCommandReg(new_address)
        sleep_ms(500)
        