import cv2
import numpy as np
import math
import time
from geometry_msgs.msg import Point
from std_msgs.msg import Int16
import rospy
import const
import opr
import pid

def pack(x):
	if x<0:
		x=abs(x)
		a=x&255
		a<<=8
	else:
		a=x&255
	return a
#mouse callback function
def getDestination(event,x,y,flags,param):
	global dst
	if event==cv2.EVENT_LBUTTONDBLCLK:
		dst.append([x,y])

#destination storing thing
dst=[]
def main():
	global dst
	rospy.init_node("main")
	pub1=rospy.Publisher("motor_vel1",Int16,queue_size=10)
	pub2=rospy.Publisher("motor_vel2",Int16,queue_size=10)

	cv2.namedWindow("image")
	cv2.namedWindow("gray")
	cap=cv2.VideoCapture(2)
	cv2.setMouseCallback("image",getDestination)
	#stores the list of points in the path
	pp1=None
	pointer=-1
	while not rospy.is_shutdown():
		ret,img=cap.read()
		if ret==0:
			cv2.waitKey(32)
			continue
		print ret
		bckup=np.copy(img)
		img=cv2.pyrDown(img)

		gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

		#cv2.imshow("gray",gray)
		cv2.waitKey(32)

		#the botpos
		pos0=opr.getCentroid(img,const.red_low,const.red_high)
		pos1=opr.getCentroid(img,const.blue_low,const.blue_high)
		if (pos0==(-1,-1,0) or pos1==(-1,-1,0)):
			cv2.waitKey(32)
			continue



		#if some destination is commanded but the path is still 
		#unknown 
		if (len(dst)>0 and pp1==None):
					
			#using blur to avoid collision with objects
			obst=cv2.inRange(img,const.obst_low,const.obst_high)
			ret, obst= cv2.threshold(obst,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
			kernel = np.ones((5,5),np.uint8)
			obst = cv2.erode(obst,kernel,iterations = 1)
			obst=cv2.medianBlur(obst,5)
			obst=cv2.blur(obst,(15,15))
			obst=cv2.GaussianBlur(obst,(9,9),0)
			obst=cv2.blur(obst,(15,15))


			#the simple path points
			pp1=opr.listPathPoints1(pos0,dst[0])
			#the actual path to be traversed
			opr.findPath(obst,pp1)

			if len(pp1)<50:
				pointer=4

			else :
				pointer =8

		#if there is some probable path found
		if pp1!=None:
			pose_err=opr.getTheta(pos0,pos1,pp1[pointer])
			if pose_err>math.pi:
				pose_err=pose_err-2*math.pi

			motor_vel=pid.getVelocity(pose_err,pos0,pp1[pointer])
			motor_vel1=motor_vel[0]
			pub1.publish(motor_vel1)
			motor_vel2=motor_vel[1]
			pub2.publish(motor_vel2)

			#flush the current target if it's too close
			if (opr.distance(pp1[pointer],pos0)<const.th_lin):
				pointer=pointer+10
			
			print len(pp1),pointer
			#if destination is reached goto next point 
			if (pointer>len(pp1)):
				pp1=None
				pub2.publish(0)
				pub1.publish(0)
				dst.pop(0)
			cv2.circle(img,(dst[0][0],dst[0][1]),3,(255,0,0),-1)

		if cv2.waitKey(32) & 0xFF==ord('q'):
			break

		cv2.circle(img,(pos0[0],pos0[1]),3,(0,0,255),-1)
		cv2.circle(img,(pos1[0],pos1[1]),3,(255,0,0),-1)		

		cv2.imshow("image",img)
		cv2.imshow("backup",bckup)
	cv2.destroyAllWindows()
	cap.release()

#IF __main__ RUN THE MAIN FUNCTION. THIS IS THE MAIN THREAD
if __name__ == '__main__':
    main()
