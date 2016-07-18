#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import sys
import math

def main():
    #video(0,'red')
    ROBOT1 = np.array([[]])
    ROBOT2 = np.array([[]])
    BALL = np.array([])

    ROBOT1 = image('btt.jpg','blue')
    ROBOT2 = image('btt.jpg','green')
    BALL = image('btt.jpg','red')
    
    print(ROBOT1)
    print(ROBOT2)
    print(BALL)

def video(camera_no,color):
    cap = cv2.VideoCapture(camera_no)
    
    xcor = np.array([])
    ycor = np.array([])

    while(1):
        xcor=[]
        ycor=[]
        count=0
        # Take each frame
        _, frame = cap.read()
        cv2.imshow('org',frame)

    
        Y, X = frame.shape[:2]
        mask = process(frame,color)

        contours,h = cv2.findContours(mask.copy(),1,2)
        no_of_contours = len(contours)
        for i in range(no_of_contours):
            cnt = contours[i]
            cnt = cv2.convexHull(cnt)
            area = cv2.contourArea(cnt)
            if area > 1000:
                M = cv2.moments(cnt)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                #cv2.circle(mask,(cx,cy), 5, (0,255,255), -1)
                (x,y),(width,height),theta = cv2.minAreaRect(cnt)
                #print(x,y,width,height,theta)
                xcor = np.append(xcor,x)
                ycor = np.append(ycor,Y-y)
                count = count+1

        if count == 2:
            midx = (xcor[0]+xcor[1])/2
            midy = (ycor[0]+ycor[1])/2
            slope = (ycor[0]-ycor[1])/(xcor[0]-xcor[1])
            theta = math.degrees(math.atan(slope))
            #print(xcor[0],ycor[0],xcor[1],ycor[1])
            print(midx,midy,theta)
            '''return np.array([(xcor[0]+xcor[1])/2, (ycor[0]+ycor[1])/2,
            (ycor[0]-ycor[1])/(xcor[0]-xcor[1]),math.degrees(math.atan(slope))])'''

        elif count == 0:
            print('0')
            pass

        elif count == 1:
            print(xcor[0],ycor[0],width,height,theta)

        
        cv2.imshow('img',mask)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
    

def image(_image,color):
    
    xcor = np.array([])
    ycor = np.array([])

    img = cv2.imread(_image)
    
    Y, X = img.shape[:2]
    mask = process(img,color)
    contours,h = cv2.findContours(mask.copy(),1,2)
    no_of_contours = len(contours)

    for i in range(no_of_contours):
        cnt = contours[i]
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        #cv2.circle(mask,(cx,cy), 5, (0,255,255), -1)
        (x,y),(width,height),theta = cv2.minAreaRect(cnt)
        #print(x,y,width,height,theta)
        xcor = np.append(xcor,x)
        ycor = np.append(ycor,Y-y)

    if no_of_contours == 2:
        midx = (xcor[0]+xcor[1])/2
        midy = (ycor[0]+ycor[1])/2
        slope = (ycor[0]-ycor[1])/(xcor[0]-xcor[1])
        theta = math.degrees(math.atan(slope))
        #print(xcor[0],ycor[0],xcor[1],ycor[1])
        #print(midx,midy,theta)
        return np.array([xcor[0],ycor[0],xcor[1],ycor[1]])
    
    elif no_of_contours == 0:
        print('xaina')

    else:
        #print(xcor[0],ycor[0],width,height,theta)
        return np.array([xcor[0],ycor[0],width,height,-theta])


    #cv2.imshow('res',mask)

    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()




def process(frame,color):

    #cv2.imshow("frame",frame)
    frame = cv2.GaussianBlur(frame, (115, 115), 0)

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

    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Bitwise-AND mask and original image
    #res = cv2.bitwise_and(frame,frame, mask= mask)
    #cv2.imshow('kaka',mask)
    return mask

if __name__=='__main__':
    main()
