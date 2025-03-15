import cv2
import numpy as np 

bajo = np.array([255,0,0])
alto = np.array([255,0,0])

z = np.zeros((400,400,3),dtype = np.uint8) + 255
cv2.circle(z,(200,200),100,(255,0,0),-1)

r = cv2.inRange(z,bajo,alto)
AND = cv2.bitwise_and(z,z,mask =r)

cv2.imshow("AND", AND)
cv2.imshow("Mascara",r)
cv2.imshow("Ventana",z)
cv2.waitKey()
