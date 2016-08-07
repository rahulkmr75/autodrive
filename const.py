import numpy as np


'''the pid constants'''
#assuming the max pixel difference is 30 
kp_lin=18
#setting it to 120 maps max to 240
kp_ang=120
#the linear velocity when angular error is not zero
k0=0.5

'''threshing values for movement of the bot'''
#thresh values for linear and angular psition for state
th_lin=3
th_ang=0.2

#colour threshing values
floor_low=np.array([28,0,107],np.uint8)
floor_high=np.array([131,75,200],np.uint8)

red_low=np.array([4,110,132],np.uint8)
red_high=np.array([30,198,172],np.uint8)

blue_low=np.array([58,91,95],np.uint8)
blue_high=np.array([131,176,151],np.uint8)
