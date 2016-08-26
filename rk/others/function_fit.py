import math
import numpy as np
import matplotlib.pyplot as plt

R = 0.033
L = 0.135

array_xy = np.array([[0,0],[0,0]])
plot_xy = plt.subplot()
error = -math.pi
for i in range(1,100,1):
 w=40*error
 if(abs(w)>=100):
    w = 100*w/abs(w)

 #v = 6/(math.exp(0.25*abs(w)+1)) 
 v = 6/((abs(w)+1)**2)

 w_l=(2*v-L*w)/(2*R)
 w_r=(2*v+L*w)/(2*R)
 array_xy = np.append(array_xy,[[w_l,w_r]],0)
 print("left and right speed") 
 print(w_l,w_r)
 error += math.pi/50;
plot_xy.scatter(array_xy[:,1],array_xy[:,0])
#plot_xy.scatter(2,3)
plt.show()
   
