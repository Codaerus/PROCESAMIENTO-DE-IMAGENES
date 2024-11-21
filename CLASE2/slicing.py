#Dividir canales

import numpy as np
import cv2

img =  cv2.imread("images.png") 
#b,g,r = cv2.split(img)
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]
cv2.imshow("Ventana de negro",img)
cv2.imshow("Ventana de azul",b)
cv2.imshow("Ventana de verde",g)
cv2.imshow("Ventana de rojo",r)
cv2.waitKey(0)
cv2.destroyAllWindows()
