import cv2
import numpy as np 

img = cv2.imread('images.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray = np.float32(gray)

dst = cv2.Canny(gray, 200, 200)
dst = cv2.dilate(dst,None)

cv2.imshow('dst',dst)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destryAllWindows()

