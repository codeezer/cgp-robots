#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import sys

def main():
    #video(0)
    #image('btest.jpg')
	detect_face()
	
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
			
			if area > 100:
							
				cx = int(M['m10']/M['m00'])
				cy = int(M['m01']/M['m00'])
				print(area)
				#hull = cv2.convexHull(cnt)
				cv2.circle(mask,(cx,cy), 5, (0,255,255), -1)
				cv2.imshow('mask',mask)
				cv2.imshow('hull',hull)
				
			else:
				cv2.imshow('mask',mask)
			
        except:
			cv2.imshow('mask',mask)
			print('except')
			
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()


def image(_image):
    img = cv2.imread(_image)
    height, width, channels = img.shape
    
    mask = process(img)
    contours,h = cv2.findContours(mask.copy(),1,2)
    
    for i in range(len(contours)):
		cnt = contours[i]
		M = cv2.moments(cnt)
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])
		cv2.circle(mask,(cx,cy), 5, (0,255,255), -1)
                (x,y),(width,height),theta = cv2.minAreaRect(cnt)
                print(x,y,width,height,theta)
    cv2.imshow('res',mask)
	
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()


def process(frame):
    
    #frame = cv2.GaussianBlur(frame, (15, 15), 0)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    # Threshold the HSV image for only green colors
    lower_green = np.array([40,70,70])
    upper_green = np.array([80,200,200])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    #mask = cv2.inRange(hsv, lower_green, upper_green)
    
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Bitwise-AND mask and original image
    #res = cv2.bitwise_and(frame,frame, mask= mask)

    return mask




def detect_face():
	
	#cascPath = "haarcascade_frontalface_default.xml"
	cascPath = "haarcascade_frontalface_alt_tree.xml"
	faceCascade = cv2.CascadeClassifier(cascPath)
	
	cap = cv2.VideoCapture(0)
	
	while(1):
		_, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		# Detect faces in the image
		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(30, 30),
			flags = cv2.cv.CV_HAAR_SCALE_IMAGE
		)
		print "Found {0} faces!".format(len(faces))
		print "The type of the faces array is {}".format(type(faces))

		# Draw a rectangle around the faces
		for (x, y, w, h) in faces:
			cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)
			
		cv2.imshow("Faces found", gray)
		
		k = cv2.waitKey(5) & 0xFF
		if k == 27:
			break
            
	cv2.destroyAllWindows()

if __name__=='__main__':
    main()
