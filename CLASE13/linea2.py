import cv2
import numpy as np

image_as_BGR = cv2.imread("h.png")
image_as_GRAY = cv2.cvtColor(image_as_BGR, cv2.COLOR_BGR2GRAY)

valor_umbral_max = 100
valor_umbral_min = 50
kernel = 3
image_with_canny = cv2.Canny(image_as_GRAY, valor_umbral_min,valor_umbral_max, apertureSize=kernel)

lineas = cv2.HoughLines(image_with_canny, rho = 1, theta = np.pi/180, threshold = 175)
print(lineas)
print(lineas[0][0][0],np.degrees(lineas[0][0][1])) # retorno es p,theta

if lineas is not None:
	for linea in lineas:
		rho,theta = linea[0]
		a = np.cos(theta)
		b = np.sin(theta)
		x0 = rho*a
		y0 = rho*b

		x1= int(x0 + 1000*(-b))
		y1= int(y0 + 1000*(a))
		x2= int(x0 - 1000*(-b))
		y2= int(y0 - 1000*(a))

		cv2.line(image_as_BGR,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow("Imagen", image_as_BGR)
cv2.imshow("Imagen con Canny",image_with_canny)
cv2.waitKey()
