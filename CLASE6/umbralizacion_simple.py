import numpy as np
import cv2

image_as_BGR = cv2.imread("random_scene.jpg")
image_as_GRAY = cv2.cvtColor(image_as_BGR, cv2.COLOR_BGR2GRAY)

valor_umbral = 127
valor_maximo = 255

ret, image = cv2.threshold(image_as_GRAY, valor_umbral, valor_maximo, cv2.THRESH_BINARY)

cv2.imshow("Ventana",image_as_GRAY)
cv2.imshow("Imagen con la umbralización",image)
cv2.waitKey()

#help(cv2.threshold)

#threshold(src, thresh, maxval, type[, dst]) -> retval, dst
