import cv2
import numpy as np
"""
b = np.zeros((256,256,3),dtype= np.uint8)+255
cv2.circle(b,(130,130),90,(255,0,0),-1)
cv2.imshow("ventana1",b)
"""

image = np.array([
			[255, 120, 50,    0],
			[200, 150, 30,  100],
			[255, 200, 128,  64],
			[0,    50, 150, 255],
], dtype = np.uint8)

mask = cv2.inRange(image,100,200)
print(mask)
AND = cv2.bitwise_and(image,mask)
print(AND)
#help(cv2.inRange)

#cv2.waitKey(0)
#inRange(src, lowerb, upperb[, dst]) -> dst
