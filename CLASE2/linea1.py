#Dibujar Linea

import numpy as np
import cv2

#help(cv2.line)

z = cv2.imread("mario.jpg",0) #np.zeros((400,400),dtype = np.uint8)
print(z.shape, z.ndim, z.dtype)
cv2.line(z,(0,0),(255,255),0,4)
print(z)
cv2.imshow("Ventana de negro",z)
cv2.waitKey(0)
cv2.destroyAllWindows()
