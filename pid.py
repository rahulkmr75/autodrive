import cv2
import math
import time
import opr
import const
from geometry_msgs.msg import Point

#for the angular and linear velocity returns in the orm of /geometry_msgs/Point
def getVelocity(ang_err,botpos,dst):
	lin_err=opr.distance(botpos,dst)
	if (ang_err>const.th_ang):
		ang_vel=const.kp_ang*(1-math.cos(ang_err))
		lin_vel=0
	elif(lin_err>const.th_lin):
		ang_vel=0
		lin_vel=const.kp_lin*lin_err
	else:
		ang_vel=0
		lin_vel=0
	motor1=int(-1*ang_vel+lin_vel)
	if motor1>150:
		motor1=150
	motor2=int(ang_vel+lin_vel)
	if motor2>150:
		motor2=150
	print lin_err,ang_err,motor1,motor2
	return (motor1,motor2)
