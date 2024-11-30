import numpy as np
import cv2

image_as_BGR = cv2.imread("mario.jpg")
image_as_GRAY = cv2.cvtColor(image_as_BGR, cv2.COLOR_BGR2GRAY)

valor_maximo = 255
metodo = cv2.ADAPTIVE_THRESH_MEAN_C
tipo = cv2.THRESH_BINARY
N = 5
C = 2
image_with_ADAPTATIVE_THRESH_MEAN_C = cv2.adaptiveThreshold(image_as_GRAY,valor_maximo,metodo,tipo,N,C)

cv2.imshow("Ventana",image_as_GRAY)
cv2.imshow("Imagen con la umbralización",image_with_ADAPTATIVE_THRESH_MEAN_C)
cv2.waitKey()


#adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) -> dst
#threshold(src, thresh, maxval, type[, dst]) -> retval, dst
