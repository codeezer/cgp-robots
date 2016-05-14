#!/usr/bin/env python
# -*- coding:utf-8 -*-
import serial

bot1 = serial.Serial('/dev/rfcomm1', 9600)
bot1.timeout = 1
# bot2 = serial.Serial('/dev/rfcomm2', 9600)

bot1.write('Something')  # Comm with bot1
# bot2.write('Something') # Comm with bot2

# bot1.readline()  # Read from bot1
# bot2.readline() # Read from bot2

# Always remember to close the serial port
# Bad things happen otherwise
bot1.close()
