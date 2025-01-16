import cv2
import numpy as np
imagen_as_BGR = cv2.imread("sudoku.jpg")
imagen_as_GRAY = cv2.cvtColor(imagen_as_BGR,cv2.COLOR_BGR2GRAY)

valor_umbral_max = 100
valor_umbral_min =50 
tamalo_kernel = 3
image_with_canny = cv2.Canny(imagen_as_GRAY,valor_umbral_min,valor_umbral_max,apertureSize=tamalo_kernel)

umbral = 175
lineas = cv2.HoughLines( image_with_canny, rho = 1, theta = np.pi/180, threshold = umbral) 
print(lineas)
for index in range(len(lineas)):
	print(index)
	rho = lineas[index][0][0]
	theta = lineas[index][0][1]

	a = np.cos(theta)
	b = np.sin(theta)

	x_0 = rho*a
	y_0 = rho*b 

	x_1 = int(x_0 + 500*(-b))
	y_1 = int(y_0 + 500*(a))

	x_2 = int(x_0 - 500*(-b))
	y_2 = int(y_0 - 500*(a))
	cv2.line(imagen_as_BGR, (x_1,y_1), (x_2,y_2), (0,255,0),2)

cv2.imshow("Imagen", imagen_as_BGR)
cv2.imshow("Imagen con Canny", image_with_canny)
cv2.waitKey(0)
