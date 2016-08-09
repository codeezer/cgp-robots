#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import math

#fgbg = cv2.BackgroundSubtractorMOG2()

def video(camera_no, color):
    cap = cv2.VideoCapture(camera_no)

    xcor = np.array([])
    ycor = np.array([])

    while(1):

        count=0
        # Take each frame
        _, frame = cap.read()
        #cv2.imshow('org',frame)

        Y, X = frame.shape[:2]
        mask = process(frame,color)

        contours,h = cv2.findContours(mask.copy(),1,2)
        no_of_contours = len(contours)
        for i in range(no_of_contours):
            cnt = contours[i]
            #cnt = cv2.convexHull(cnt)
            area = cv2.contourArea(cnt)
            print(area)
            if area > 250:
                M = cv2.moments(cnt)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                #cv2.circle(mask,(cx,cy), 5, (0,255,255), -1)
                (x,y),(width,height),theta = cv2.minAreaRect(cnt)
                #print(x,y,width,height,theta)
                xcor = np.append(xcor,x)
                ycor = np.append(ycor,Y-y)

                count = count+1


        if count == 0:
            pass


        elif count == 2:
            midx = (xcor[0]+xcor[1])/2
            midy = (ycor[0]+ycor[1])/2
            slope = (ycor[0]-ycor[1])/(xcor[0]-xcor[1])
            theta = math.degrees(math.atan(slope))
            #print(xcor[0],ycor[0],xcor[1],ycor[1])
            return([xcor[0],ycor[0],xcor[1],ycor[1], midx, midy, theta])
            #print(midx,midy,theta)
            #return([midx,midy,theta])


        elif count == 1:
            #print(xcor[0],ycor[0],width,height,theta)
            return([xcor[0],ycor[0],width,height])
            #pass


        #cv2.imshow('img',mask)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()



def process(frame,color):

    #cv2.imshow("frame",frame)
    #frame = cv2.GaussianBlur(frame, (15, 15), 0)
    frame = cv2.blur(frame,(5,5))
    #frame = cv2.medianBlur(frame, 5)
    #frame = cv2.bilateralFilter(frame,9,75,75)

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
        upper_green = np.array([80,200,200])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_green, upper_green)
        #cv2.imshow('mask',mask)


    if color == 'red':
        # lower mask (0-10)
        lower_red = np.array([0,110,90])
        upper_red = np.array([10,255,255])
        mask0 = cv2.inRange(hsv, lower_red, upper_red)

        # upper mask (170-180)
        lower_red = np.array([170,110,50])
        upper_red = np.array([180,255,255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)

        
        # join my masks
        mask = mask0+mask1
    #mask = fgbg.apply(mask)
    #mask = cv2.GaussianBlur(mask,(5,5),0)

    mask = cv2.dilate(mask, None, iterations=3)
    mask = cv2.erode(mask, None, iterations=3)
    #mask = cv2.dilate(mask, None, iterations=2)

    # Bitwise-AND mask and original image
    #res = cv2.bitwise_and(frame,frame, mask= mask)
    #cv2.imshow('kaka',mask)
    return mask





#for images

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
        print(midx,midy,theta)
        return np.array([xcor[0],ycor[0],xcor[1],ycor[1]])

    elif no_of_contours == 0:
        #print('xaina')
        return np.array([])

    else:
        #print(xcor[0],ycor[0],width,height,theta)
        return np.array([xcor[0],ycor[0],width,height,-theta])


    #cv2.imshow('res',mask)

    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
