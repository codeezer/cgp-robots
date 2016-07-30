import numpy as np
from pd import track
import time
import math

def main():

	#scaling factors
	#sfx = 30.0/140.0
	#sfy = 30.0/144.0

	#scaling factors
	sfx = 30.0/148.0
	sfy = 30.0/144.0

	y_off = 2/sfy

	ball = np.array([])
	robot1 = np.array([])
	robot2 = np.array([])

	'''
	#get robot1 position
	#(x1,y1,x2,y2,x,y,theta)
	robot1 = track.video(1, 'red')
	print(robot1)
	print(sfx*robot1[0], sfy*robot1[1], sfx*robot1[2], sfy*robot1[3], sfx*robot1[4], sfy*robot1[5], robot1[6])
	dx = robot1[2] - robot1[0]
	dy = robot1[3] - robot1[1]
	d = math.sqrt(pow(dx,2) + pow(dy,2))
	da = math.sqrt(pow(sfx*dx,2) + pow(sfy*dy,2))
	print(dx, dy, d, sfx*dx, sfy*dy, da)
	print('\n')
	#get robot2 position
	#(x1,y1,x2,y2,x,y,theta)
	#robot2 = track.video(1, 'green')
	#print(robot2[6])

	'''

	#get ball's position
	#(x,y,w,h)
	ball = track.video(2, 'red')
	#print(ball)
	print(sfx*ball[0], sfy*ball[1], sfx*ball[2], sfy*ball[3])

	time.sleep(5)
	#get ball's position
	#(x,y,w,h)
	ball = track.video(2, 'red')
	#print(ball)
	print(sfx*ball[0], sfy*ball[1], sfx*ball[2], sfy*ball[3])

	
	#robot1 = track.video(1, 'red')
	#print(robot1)
	#print(sfx*(robot1[2]-robot1[0]))
	#to track robot track.video(camera_no, color_name_in_string)
	#returns numpy array of position and orientation of robot

	'''
	ROBOT1 = np.array([[]])
	ROBOT2 = np.array([[]])
	BALL = np.array([])

	ROBOT1 = track.image('btt.jpg','blue')
	ROBOT2 = track.image('btt.jpg','green')
	BALL = track.image('btt.jpg','red')

	print(ROBOT1)
	print(ROBOT2)
	print(BALL)
	'''

if __name__=='__main__':
	main()
