#Dibujar Linea y rectangulo

import numpy as np
import cv2

help(cv2.circle)

z =  np.zeros((400,400,3),dtype = np.uint8) #cv2.imread("mario.jpg",1) 
print(z.shape, z.ndim, z.dtype)
cv2.rectangle(z,(10,10),(200,200),(0,0,255),4)
cv2.line(z,(10,10),(200,200),(0,0,255),4)
cv2.circle(z,(200,200),60,(0,255,0),8)
#print(z)
cv2.imshow("Ventana de negro",z)
cv2.waitKey(0)
cv2.destroyAllWindows()


#line(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
#rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
#circle(img, center, radius, color[, thickness[, lineType[, shift]]]) -> img
