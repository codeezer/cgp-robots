#!/usr/bin/env python
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()

ax1 = fig.add_subplot(1,1,1)

ax1.spines["top"].set_visible(False)
ax1.spines["bottom"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.spines["left"].set_visible(False)

ax1.set_xlim([-100,100])
ax1.set_ylim([-100,100])

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
def animate(i):
    pullData = open("sampleText.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar,yar,color = 'r')

def main():
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()


if __name__=='__main__':
    main()
