import cv2
import numpy as np

img = cv2.imread("mario.jpg",0) 
#print(img.shape)
b = np.zeros((256,256),dtype= np.uint8)
#cv2.rectangle(b,(80,80),(180,180),255,-1)
#b[80:200,80:200] = 255;
cv2.circle(b,(130,130),90,255,-1)

AND = cv2.bitwise_and(img,b)
OR = cv2.bitwise_or(img,b)

cv2.imshow("ventana1",img)
cv2.imshow("ventana2",b)
cv2.imshow("AND",AND)
cv2.imshow("OR",OR)

cv2.waitKey(0)
