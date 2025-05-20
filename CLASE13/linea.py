import cv2
import numpy as np

image_as_BGR = cv2.imread("h.png")
image_as_GRAY = cv2.cvtColor(image_as_BGR, cv2.COLOR_BGR2GRAY)

valor_umbral_max = 100
valor_umbral_min = 50
kernel = 3
image_with_canny = cv2.Canny(image_as_GRAY, valor_umbral_min,valor_umbral_max, apertureSize=kernel)

lineas = cv2.HoughLines(image_with_canny, rho = 1, theta = np.pi/180, threshold = 175)
print(lineas[0][0][0],np.degrees(lineas[0][0][1])) # retorno es p,theta

cv2.imshow("Imagen", image_as_BGR)
cv2.imshow("Imagen con Canny",image_with_canny)
cv2.waitKey()
