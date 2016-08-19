import numpy as np


'''the pid constants'''
#assuming the max pixel difference is 30 
kp_lin=14
#setting it to 120 maps max to 240
kp_ang=150 
#the linear velocity when angular error is not zero
k0=0.5

'''threshing values for movement of the bot'''
#thresh values for linear and angular psition for state
th_lin=8
th_ang=0.3

#colour threshing values
obst_low=np.array([20,40,0],np.uint8)
obst_high=np.array([50,180,160],np.uint8)

red_low=np.array([0,120,100],np.uint8)
red_high=np.array([20,255,180],np.uint8)

blue_low=np.array([50,40,90],np.uint8)
blue_high=np.array([70,255,170],np.uint8)
