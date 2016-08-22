import numpy as np
from pd import track
import time
import math

def main():

    #scaling factors
    #sfx = 30.0/140.0
    #sfy = 30.0/144.0

    #scaling factors
    sfx = 30.0/152.0
    sfy = 30.0/152.0

    tfx = 68
    tfy = 60

    y_off = 2/sfy

    ball = np.array([])
    robot1 = np.array([])
    robot2 = np.array([])

    for i in range(100):
    	ball = track.video(1,'red')
    #print(ball)
    	print(str(int(sfx*(ball[0]-tfx)))+','+str(int(sfy*(ball[1]-tfy))))

    #ball = track.video(1,'red')
    #print(ball)
    #print(str(int(sfx*(ball[0]-tfx)))+','+str(int(sfy*(ball[1]-tfy))))

    '''
    #get ball's position
    #(x,y,w,h)
    ball = track.video(1, 'red')
    #print(ball)
    print(sfx*ball[0], sfy*ball[1], sfx*ball[2], sfy*ball[3])

    time.sleep(5)
    #get ball's position
    #(x,y,w,h)
    ball = track.video(1, 'red')
    #print(ball)
    print(sfx*ball[0], sfy*ball[1], sfx*ball[2], sfy*ball[3])
    '''
	
if __name__=='__main__':
	main()
