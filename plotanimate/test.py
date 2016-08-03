#!/usr/bin/env python
# -*- coding:utf-8 -*-
import serial
import matplotlib.pyplot as plt
import numpy as np

#array_xy = np.array([[0,0],[0,0]])
#plot_xy = plt.subplot()
def write2file(x,y):
    f = open("sampleText.txt","a")
    f.write(str(x)+','+str(y)+'\n')
    f.close()


bot1 = serial.Serial('/dev/ttyACM1', 9600)
bot1.timeout = 1
bot1.flush()
x = 0
# bot2 = serial.Serial('/dev/rfcomm2', 9600)
#for i in range(0,100):
while(1):
    try:
        line = bot1.readline()
        if float(line.strip()) != 0:
            y = line.strip()
            #array_xy = np.append(array_xy,[[i,float(line.strip())]],0)
            write2file(x,y)
            #k.append(line.strip())
            x = x+1
            if x > 200:
                x = 0
    except:
        pass

#plot_xy.plot(array_xy[:,0],array_xy[:,1])
#plt.show()
