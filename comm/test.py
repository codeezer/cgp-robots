#!/usr/bin/env python
# -*- coding:utf-8 -*-
import serial
import matplotlib.pyplot as plt
import numpy as np

array_xy = np.array([[0,0],[0,0]])
plot_xy = plt.subplot()


bot1 = serial.Serial('/dev/ttyACM1', 9600)
bot1.timeout = 1
bot1.flush()
# bot2 = serial.Serial('/dev/rfcomm2', 9600)
k = []
for i in range(0,100):
    try:
        line = bot1.readline()
        if float(line.strip()) != 0:
            array_xy = np.append(array_xy,[[i,float(line.strip())]],0)
            #k.append(line.strip())
    except:
        pass

plot_xy.plot(array_xy[:,0],array_xy[:,1])
plt.show()
# bot2.write('Something') # Comm with bot2

# bot1.readline()  # Read from bot1
# bot2.readline() # Read from bot2

# Always remember to close the serial port
# Bad things happen otherwise
# bot1.close()
