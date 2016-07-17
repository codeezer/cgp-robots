#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import sys
import math

def main():
    #video(0)
    print("ROBOT1")
    image('btt.jpg','blue')
    print("ROBOT2")
    image('btt.jpg','green')
    print("BALL")
    image('btt.jpg','red')
    

def video(camera_no):
    cap = cv2.VideoCapture(camera_no)

    while(1):
        # Take each frame
        _, frame = cap.read()
        mask = process(frame,'blue')
        try:
            contours,h = cv2.findContours(mask.copy(),1,2)
            cnt = contours[0]
            M = cv2.moments(cnt)
            area = cv2.contourArea(cnt)
            print(len(contours))
            cx = int(M['m10']/M['m00'])
            if area > 100:
                cy = int(M['m01']/M['m00'])
                #hull = cv2.convexHull(cnt)
                #cv2.circle(mask,(cx,cy), 5, (0,255,255), -1)
                #(x,y),(width,height),theta = cv2.minAreaRect(cnt)
                print(x,y,width,height,theta)
                cv2.imshow('mask',mask)
                #cv2.imshow('hull',hull)
            else:
                cv2.imshow('mask',mask)
                print('except')
        except:
            cv2.imshow('mask',mask)
            #print('except')

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()


def image(_image,color):
    img = cv2.imread(_image)
    height, width, channels = img.shape
    mask = process(img,color)
    contours,h = cv2.findContours(mask.copy(),1,2)

    xcor=[]
    ycor=[]
    no_of_contours = len(contours)

    for i in range(no_of_contours):
        cnt = contours[i]
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.circle(mask,(cx,cy), 5, (0,255,255), -1)
        (x,y),(width,height),theta = cv2.minAreaRect(cnt)
        #print(x,y,width,height,theta)
        xcor.append(x)
        ycor.append(y)

    if no_of_contours == 2:
        midx = (xcor[0]+xcor[1])/2
        midy = (ycor[0]+ycor[1])/2
        slope = (ycor[0]-ycor[1])/(xcor[0]-xcor[1])
        theta = math.degrees(math.atan(slope))
        print(midx,midy,theta)

    else:
        print(x,y,width,height,theta)


    #cv2.imshow('res',mask)

    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()


def process(frame,color):

    cv2.imshow("frame",frame)
    frame = cv2.GaussianBlur(frame, (15, 15), 0)
    #cv2.imshow("frame",frame)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #cv2.imshow("frame",hsv)
    if color == 'blue':
        # define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

    elif color == 'green':
        # Threshold the HSV image for only green colors
        lower_green = np.array([40,70,70])
        upper_green = np.array([80,255,255])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_green, upper_green)
        #cv2.imshow('mask',mask)

    if color == 'red':
        # lower mask (0-10)
        lower_red = np.array([0,50,50])
        upper_red = np.array([10,255,255])
        mask0 = cv2.inRange(hsv, lower_red, upper_red)

        # upper mask (170-180)
        lower_red = np.array([170,50,50])
        upper_red = np.array([180,255,255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)

        # join my masks
        mask = mask0+mask1

    #mask = cv2.erode(mask, None, iterations=2)
    #mask = cv2.dilate(mask, None, iterations=2)

    # Bitwise-AND mask and original image
    #res = cv2.bitwise_and(frame,frame, mask= mask)

    return mask

if __name__=='__main__':
    main()
