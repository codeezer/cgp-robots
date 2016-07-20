import numpy as np
from pd import track
import time

def main():

	
	
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