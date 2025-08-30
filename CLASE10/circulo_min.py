import cv2
import numpy as np
image_as_BGR = cv2.imread("image_2.png")
image_as_GRAY = cv2.cvtColor(image_as_BGR, cv2.COLOR_BGR2GRAY)

valor_umbral = 127
valor_maximo = 255
tipo = cv2.THRESH_BINARY
ret, image_with_threshold = cv2.threshold(image_as_GRAY,valor_umbral, valor_maximo, tipo)
contours, hierarchy = cv2.findContours(image_with_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

(x,y), radius = cv2.minEnclosingCircle(contours[0])

center = (int(x), int(y))
radius = int(radius)
color = (0,255,0)

cv2.circle(image_as_BGR, center, radius,color,2)
cv2.imshow("Imagen", image_as_BGR)
cv2.waitKey()
