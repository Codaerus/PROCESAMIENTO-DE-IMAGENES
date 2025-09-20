import cv2
import numpy as np

image_as_BGR = cv2.imread("coins.jpg")
image_as_GRAY = cv2.cvtColor(image_as_BGR,cv2.COLOR_BGR2GRAY)

##################### UMBRALIZACIÓN #########################
tipo = cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
valor_maximo = 255
valor_umbral = 0
ret, image_with_threshold =  cv2.threshold(image_as_GRAY,valor_umbral, valor_maximo,tipo)
#################### APERTURA MORFOLOGIA (Eliminación de ruido) ##########################
kernel = np.ones((3,3), np.uint8)
image_with_opening = cv2.morphologyEx(image_with_threshold, cv2.MORPH_OPEN, kernel, iterations = 3)
#################### IDENTIFICACIÓN DE FONDO SEGURO #############################
background = cv2.dilate(image_with_opening,kernel,iterations = 3)
################### Transformada de distancia (DT) ##############################
distanceTransform = cv2.distanceTransform(image_with_opening, cv2.DIST_L2, 5)
cv2.normalize(distanceTransform, distanceTransform,1,0,cv2.NORM_INF)
############# Umbralización del DT para obtener el primer plano seguro ##########
valor_umbral = 0.7*distanceTransform.max()
"""
>0.9  Detectas solo el centro puro
<0.5 incluir borden o zonas cercanas al fondo
0.7 es un buen balance entre precisión y cobertura del objeto
"""
ret, foreground = cv2.threshold(distanceTransform, valor_umbral,255, cv2.THRESH_BINARY)
########################## ZONA DESCONOCIDA ####################################
foreground = np.uint8(foreground)
image = cv2.subtract(background, foreground)
################### Preparación de los marcadores ##############################
return_value, markers = cv2.connectedComponents(foreground)
markers = markers + 1
markers[image == 255] = 0 #Marca la zona desconocida con el valor de cero
                          #Watershed decidirá si estas zonas son fondo o parte del objeto
"""
Fondo Seguro 1
Objeto seguro 2,3,4,...
Zona desconocida 0
Bordes -1
"""
############################### Watersheed ##################################
markers = cv2.watershed(image_as_BGR, markers) 
image_as_BGR[markers == -1] = [0,255,0] #Marca los bordes entre las diferentes regiones con el color verde
############################### Coloreado ####################################
min_value, max_value, min_value_cordinate, max_value_cordinate = cv2.minMaxLoc(markers)
markers = 255*(markers - min_value)/(max_value - min_value)
markers = np.uint8(markers)
markers = cv2.applyColorMap(markers, cv2.COLORMAP_JET)
##############################################################################
cv2.imshow("Background ", background )
cv2.imshow("Foreground", foreground)
cv2.imshow("image", image)
cv2.imshow("BGR", image_as_BGR)
cv2.imshow("markers", markers)
cv2.waitKey()
