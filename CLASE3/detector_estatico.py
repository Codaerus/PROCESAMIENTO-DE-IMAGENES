import cv2
import numpy as np 

bajo = np.array([100,80,80]) #HSV
alto = np.array([126,255,255])

z = cv2.imread("images.jpg")#np.zeros((400,400,3),dtype = np.uint8) + 255
#cv2.circle(z,(200,200),100,(255,0,0),-1)
z_HSV = cv2.cvtColor(z,cv2.COLOR_BGR2HSV)
r = cv2.inRange(z_HSV ,bajo,alto)
AND = cv2.bitwise_and(z,z,mask =r)

cv2.imshow("AND", AND)
cv2.imshow("Mascara",r)
cv2.imshow("Ventana",z)
cv2.waitKey()
