import cv2
import math
import opr
import time
from PIL import Image

img = cv2.imread('f1.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print time.time()
gline=cv2.blur(img,(15,15))
gline=cv2.blur(img,(15,15))
gline=cv2.GaussianBlur(gline,(9,9),0)
gline=cv2.blur(gline,(15,15))
gline=cv2.pyrDown(gline)
#gline=cv2.pyrDown(gline)

#obstacle=findGradient(gline)
ret, obstacle = cv2.threshold(gline,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


#points on the path
pp1=opr.listPathPoints1((80,228),(314,48))
#print len(pp1)

#l=opr.getSecondaryPath(obstacle,[128,107],[110,74])
#print (l)
#print pp1

opr.findPath(obstacle,pp1)
#findPath1(obstacle,pp1)

'''for i in pp1:
    obstacle=cv2.circle(obstacle,(i[0],i[1]),10,(255,0,0),-1)'''


print time.time()
cv2.imshow("gline",gline)
cv2.imshow("obstacle",obstacle)
#cv2.imshow("obstacle1",obstacle1)
#cv2.imshow("otsu",otsu)
#cv2.imshow("path",path)
cv2.waitKey(0)

