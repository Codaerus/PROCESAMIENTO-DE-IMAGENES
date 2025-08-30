import cv2
import numpy as np
image_as_BGR = cv2.imread("image_2.png")
image_as_GRAY = cv2.cvtColor(image_as_BGR, cv2.COLOR_BGR2GRAY)

valor_umbral = 127
valor_maximo = 255
tipo = cv2.THRESH_BINARY
#help(cv2.moments)
ret, image_with_threshold = cv2.threshold(image_as_GRAY,valor_umbral, valor_maximo, tipo)
contours, hierarchy = cv2.findContours(image_with_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#######################  CUADRO ROTADO ########################
(x,y),(w,h), angle = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(((x,y),(w,h), angle))
box = np.int64(box)
######################## CUADRO RECTO ##########################
x,y,w,h = cv2.boundingRect(contours[0])
start_point = (x,y)
end_point = (x+w,y+h)
color = (0,255,0)
######################## ENVOLTURA CONVEXA #####################
convex_hull = cv2.convexHull(contours[0])
######################## Relación de aspecto ###################
aspect_ratio = w/h
print("Relación de aspecto",aspect_ratio)
######################## EXTENSIÓN #############################
contour_area = cv2.contourArea(contours[0]) #área del contorno
bounding_rectangle_area = w*h #área del cuadro recto
extent = contour_area/bounding_rectangle_area
print("Extensión: ",extent)
######################## SOLIDEZ ###############################
convex_hull_area = cv2.contourArea(convex_hull)
solidity = contour_area/convex_hull_area
print("Solidez: ",solidity)
######################## DIAMETRO EQUIVALENTE ##################
equivalent_diameter = np.sqrt(4*contour_area/np.pi)
print("Diámetro equivalente: ", equivalent_diameter)
################################################################
cv2.drawContours(image_as_BGR,[box],-1,(0,255,255),4)
cv2.rectangle(image_as_BGR,start_point,end_point,color,2)
cv2.drawContours(image_as_BGR,[convex_hull],-1,(0,0,255),4)
cv2.imshow("Imagen", image_as_BGR)
cv2.waitKey()
