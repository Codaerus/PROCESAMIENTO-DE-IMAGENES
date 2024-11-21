import cv2
import numpy as np

img = cv2.imread("mario.jpg",0) 
#print(img.shape)
b = np.zeros((256,256),dtype= np.uint8)
cv2.rectangle(b,(80,80),(180,180),255,-1)
AND = cv2.bitwise_and(img,b)

cv2.imshow("ventana1",img)
cv2.imshow("ventana2",b)
cv2.imshow("AND",AND)

cv2.waitKey(0)
