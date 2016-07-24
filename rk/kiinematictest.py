import math
from random import gauss
import numpy as np
import matplotlib.pyplot as plt

#constants and initialization lengths in cm
R = 3.3
L = 13.5

x = 0
y = 10

array_xy = np.array([[0,0],[0,0]])
plot_xy = plt.subplot()

phi = 0
goal_x=100
goal_y=100
v_max = 5
scalingfactor = 1

vel_robot=0
omega_robot=0

for i in range(1,100,1):
 omega_left= (2*vel_robot-L*omega_robot)/(2*R)
 omega_right=(2*vel_robot+L*omega_robot)/(2*R)

 #del_encoder_left = 30
 #del_encoder_right = 29

 #left_wheel_distance = 2*math.pi*R*del_encoder_left/60
 #right_wheel_distance = 2*math.pi*R*del_encoder_right/60
 #distance_centre = (left_wheel_distance + right_wheel_distance)/2

 #x += distance_centre*math.cos(phi)
 #y += distance_centre*math.sin(phi)
 #phi += (right_wheel_distance-left_wheel_distance)/L

 x += vel_robot*math.cos(phi)+gauss(0,0)
 y += vel_robot*math.cos(phi)+gauss(0,0)
 phi += omega_robot+gauss(0,0)



 print x,y
 array_xy = np.append(array_xy,[[x,y]],0)

 del_phi = math.atan((goal_y - y)/(goal_x - x)) - phi  # approximation of tangent used
 omega_robot = scalingfactor*del_phi
 vel_robot =  v_max/(omega_robot+1)**2

plot_xy.scatter(array_xy[:,1],array_xy[:,0])
#plot_xy.scatter(2,3)
plt.show()
