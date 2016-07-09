#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import sys

def main():
    #video(0)
    print("ROBOT1")
    image('btt.jpg','blue')
    print("ROBOT2")
    image('btt.jpg','green')


def video(camera_no):
    cap = cv2.VideoCapture(camera_no)

    while(1):
        # Take each frame
        _, frame = cap.read()
        mask = process(frame)
        try:
            contours,h = cv2.findContours(mask.copy(),1,2)
            cnt = contours[0]
            M = cv2.moments(cnt)
            area = cv2.contourArea(cnt)
            print(len(contours))
            if area > 100:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                #hull = cv2.convexHull(cnt)
                #cv2.circle(mask,(cx,cy), 5, (0,255,255), -1)
                #(x,y),(width,height),theta = cv2.minAreaRect(cnt)
                print(x,y,width,height,theta)
                cv2.imshow('mask',mask)
                #cv2.imshow('hull',hull)
            else:
                cv2.imshow('mask',mask)
        except:
            cv2.imshow('mask',mask)
            print('except')

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
    for i in range(len(contours)):
        cnt = contours[i]
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.circle(mask,(cx,cy), 5, (0,255,255), -1)
        (x,y),(width,height),theta = cv2.minAreaRect(cnt)
        '''if theta ==0:
            xcor.append(x);
            ycor.append(y);
        '''
        xcor.append(x)
        ycor.append(y)
        print(x,y,width,height,theta)

    try:
        midx = (xcor[0]+xcor[1])/2
        midy = (ycor[0]+ycor[1])/2
        slope = (ycor[0]-ycor[1])/(xcor[0]-xcor[1])
        print(midx,midy,slope)


    except:
        print("no more contour")

    #cv2.imshow('res',mask)

    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()


def process(frame,color):

    frame = cv2.GaussianBlur(frame, (5, 5), 0)
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

    #mask = cv2.erode(mask, None, iterations=2)
    #mask = cv2.dilate(mask, None, iterations=2)

    # Bitwise-AND mask and original image
    #res = cv2.bitwise_and(frame,frame, mask= mask)

    return mask

if __name__=='__main__':
    main()
