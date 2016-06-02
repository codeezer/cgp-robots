#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()
    
    # Convert BGR to GRAY
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#    can = cv2.Canny(gray, 200, 200)
#    can = cv2.dilate(can,None)
#    cv2.imshow('can',can)
    gray = np.float32(gray)
    harris = cv2.cornerHarris(gray,2,3,0.08)
    harris = cv2.dilate(harris,None)
    #frame[harris>0.01*harris.max()]=[0,0,255]
    cv2.imshow('harris',harris)
    cv2.imshow('cam',frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
