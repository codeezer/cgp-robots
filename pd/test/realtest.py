import numpy as np
import track
import time
import math

def main():

	ROBOT1 = np.array([[]])
	ROBOT2 = np.array([[]])
	BALL = np.array([])

	ROBOT1 = track.image('two.jpg','blue','robotb')
	ROBOT2 = track.image('two.jpg','green','robotg')
	BALL = track.image('two.jpg','red','ball')

	#print(ROBOT1)	
	#print(ROBOT2)
	#print(BALL)
	
	print("\n POSITION of ROBOTB: ("+str(ROBOT1[4])+","+str(ROBOT1[5])+") => ("+str(ROBOT1[4]*30/140)+" cm,"+str(ROBOT1[5]*30/144)+" cm)")
	print("\n ORIENTATION of ROBOTB: "+str(ROBOT1[6]))
	
	print("\n\n POSITION of ROBOTG: ("+str(ROBOT2[4])+","+str(ROBOT2[5])+") => ("+str(ROBOT2[4]*30/140)+"cm ,"+str(ROBOT2[5]*30/144)+" cm)")
	print("\n ORIENTATION of ROBOTG: "+str(ROBOT2[6]))
	
	print("\n\n POSITION OF BALL: ("+str(BALL[0])+","+str(BALL[1])+") => ("+str(BALL[0]*30/140)+"cm ,"+str(BALL[1]*30/144)+" cm)")
	print("\n")

if __name__=='__main__':
	main()
