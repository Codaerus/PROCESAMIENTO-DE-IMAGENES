import cv2
import numpy as np
image_as_BGR = cv2.imread("coins.jpg")
image_as_GRAY = cv2.cvtColor(image_as_BGR, cv2.COLOR_BGR2GRAY)

tipo = cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
valor_maximo = 255
valor_umbral = 0
return_value, image_with_threshold = cv2.threshold(image_as_GRAY,valor_umbral,valor_maximo,tipo)

kernel = np.ones((3,3), np.uint8)
image_with_opening = cv2.morphologyEx(image_with_threshold,cv2.MORPH_OPEN, kernel, iterations = 3)

background = cv2.dilate(image_with_opening,kernel,iterations=3)

distance_transform = cv2.distanceTransform(image_with_opening,cv2.DIST_L1,5)
cv2.normalize(distance_transform,distance_transform,1,0,cv2.NORM_INF)

tipo = cv2.THRESH_BINARY
valor_maximo = 255
valor_umbral = 0.7*distance_transform.max()
return_value, foreground = cv2.threshold(distance_transform,valor_umbral,valor_maximo,tipo)
foreground = np.uint8(foreground)
image = cv2.subtract(background,foreground) # fondo(dilatado), objeto(TD+umbral)
#La resta genera una franja que es la zona desconocida
return_value, markers = cv2.connectedComponents(foreground)
markers = markers + 1
markers[image==255] = 0 #Marcamos zona desconocida para que W decida si es fondo u objeto
print(return_value)
print(set(markers.flatten().tolist()))
"""
Para que watersheed pueda trabajar:
Zonas ya clasificadas
	Fondo seguro (label 1)
	Objetos seguros (label 2,3,etc)
Zona sin clasificar (desconocidas)
	Se marcan con 0 en markers
"""
markers = cv2.watershed(image_as_BGR, markers)
image_as_BGR[markers==-1] = [0,255,0]

min_value, max_value, min_value_coordinate, max_value_coordinate = cv2.minMaxLoc(markers)

markers = 255*(markers-min_value)/(max_value-min_value)
markers = np.uint8(markers)

markers = cv2.applyColorMap(markers,cv2.COLORMAP_JET)

cv2.imshow("Imagen", background)
cv2.imshow("Image", markers)
cv2.imshow("Resta", image)
cv2.imshow("foreground", foreground)
cv2.imshow("Imagen en BGR", image_as_BGR)
cv2.imshow("Imagen con TD", distance_transform)
cv2.waitKey(0)
