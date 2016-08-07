import cv2
import numpy as np
import math




def findBotPose(bgr,point):
	#the orientation of the bot is decided by a red and a blue colored circle acting as an arrowhead pointing towards the direction of movement (red--blue-->)

	hsv=cv2.cvtColor(bgr,cv2.COLOR_BGR2HSV)

	#red
	img = cv2.inRange(hsv,(0,170,0),(14,255,255))

	moments = cv2.moments(img)
	m00 = moments['m00']
	c1_x, c1_y = None, None
	if m00 != 0:
	    c1_x = int(moments['m10']/m00)
	    c1_y = int(moments['m01']/m00)
	#print c1_x,c1_y
	#blue
	hsv=cv2.cvtColor(bgr,cv2.COLOR_BGR2HSV)
	img = cv2.inRange(hsv,(140,94,74),(199,255,148))

	moments = cv2.moments(img)
	m00 = moments['m00']
	c2_x, c2_y = None, None
	if m00 != 0:
	    c2_x = int(moments['m10']/m00)
	    c2_y = int(moments['m01']/m00)
	#print c2_x,c2_y
	theta_diff = math.acos(float((c2_y-c1_y)*(point[1]-c1_y)+(c2_x-c1_x)*(point[0]-c1_x))/(math.sqrt((c2_x-c1_x)**2+(c2_y-c1_y)**2)*(math.sqrt((point[0]-c1_x)**2+(point[1]-c1_y)**2))))*180/math.pi

	#print theta_diff,((c1_x+c2_x)/2,(c1_y+c2_y)/2)
	return theta_diff,((c1_x+c2_x)/2,(c1_y+c2_y)/2)
	
cap=cv2.VideoCapture(0)
while True:
	ret,bgr=cap.read()
	theta,pos=findBotPose(bgr,(320,240))
	print theta
	bgr=cv2.circle(bgr,pos,5,(255,0,0),-1)
	cv2.imshow("window",bgr)
	if cv2.waitKey(30) & 0xff==ord('q'):
		break
cv2.destroyAllWindows()
cap.release()

