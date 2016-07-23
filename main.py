import numpy as np
from pd import track
import time

def main():

	ball = np.array([])
	robot1 = np.array([])
	robot2 = np.array([])

	#get robot1 position
	#(x1,y1,x2,y2,x,y,theta)
	robot1 = track.video(0, 'blue', 1)	


	#get robot2 position
	#(x1,y1,x2,y2,x,y,theta)
	robot2 = track.video(0, 'green', 1)

	#get ball's position
	#(x,y,w,h,theta)
	ball = track.video(0, 'red', 0)

	#scaling factors
	sfx = 30.0/140.0
	sfy = 30.0/144.0

	

	#to track robot track.video(camera_no, color_name_in_string)
	#returns numpy array of position and orientation of robot

	'''
	ret_val = np.array([])
	ret_val = track.video(0,'red')
	print(ret_val)
	time.sleep(5)
	ret_val = track.video(0,'red')
	print(ret_val)

	print(ret_val)

	ret_val = track.video(0,'blue')
	print(ret_val)

	ret_val = track.video(0,'green')
	print(ret_val)
	'''

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
