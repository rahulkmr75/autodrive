import cv2
import numpy as np


img = cv2.imread('f1.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gline=cv2.medianBlur(img,5)
gline=cv2.GaussianBlur(gline,(9,9),0)
gline=cv2.blur(gline,(15,15))
gline=cv2.pyrDown(gline)
cv2.imshow("window",gline)
cv2.waitKey(3000)