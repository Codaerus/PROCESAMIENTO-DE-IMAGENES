import numpy as np
import cv2

image_as_BGR = cv2.imread("image.png")
image_as_GRAY = cv2.cvtColor(image_as_BGR, cv2.COLOR_BGR2GRAY)

valor_maximo = 255
valor_umbral = 100
tipo = cv2.THRESH_BINARY

ret_value, image_with_THRESH_BINARY = cv2.threshold(image_as_GRAY,valor_umbral,valor_maximo,tipo)
cv2.imshow("Ventana",image_as_GRAY)
cv2.imshow("Imagen con la umbralización",image_with_THRESH_BINARY)
cv2.waitKey()
