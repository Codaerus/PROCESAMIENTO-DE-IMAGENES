import cv2
import numpy as np
#help(cv2.findContours)
image_as_BGR = cv2.imread("manzana.jpg")
image_as_GRAY = cv2.cvtColor(image_as_BGR, cv2.COLOR_BGR2GRAY)
image_as_GRAY = cv2.GaussianBlur(image_as_GRAY,(7,7),0)
#Umbral Adaptativo
image_thresh = cv2.adaptiveThreshold(image_as_GRAY,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
####################################
contours, hierarchy = cv2.findContours(image_thresh ,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
print(len(contours))
########## CUADRO RECTO ############
x,y,w,h = cv2.boundingRect(contours[0])
start_points = (x,y)
end_points = (x+w,y+h)
color = (0,255,0)
######## CUADRO ROTADO ############
(x,y), (w,h), angle = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(((x,y), (w,h), angle))
box = np.int64(box)
print(box)
##################################
cv2.rectangle(image_as_BGR,start_points,end_points,color,2) #Cuadro recto
cv2.drawContours(image_as_BGR,contours,-1,(0,255,0),2) 
cv2.drawContours(image_as_BGR,[box],-1,(255,0,0),4)       #Cuadro rotado
cv2.imshow("Manzana1", image_thresh)
cv2.imshow("Manzana2", image_as_BGR)
cv2.waitKey(0)
