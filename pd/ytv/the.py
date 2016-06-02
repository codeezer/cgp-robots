import cv2
import numpy as np

img = cv2.imread('the.jpg',0)

ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh.copy(), 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)
#print M
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
#cnt = contours[2]
#cv2.drawContours(img, [cnt], 0, (0,255,0), 3)
#rect = cv2.minAreaRect(cnt)
(x,y),(width,height),theta = cv2.minAreaRect(cnt)
print(theta)


#box = cv2.boxPoints(rect)
#box = np.int0(box)
#cv2.drawContours(img,[box],0,(255,0,0),2)
cv2.imshow('img',img)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
