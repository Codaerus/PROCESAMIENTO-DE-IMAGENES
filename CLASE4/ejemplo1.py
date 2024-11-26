import cv2
import numpy

image_as_BGR  = cv2.imread("images.png")

image_as_BGR_copy = image_as_BGR.copy()
image_as_BGR_copy[:,:,1] = 0 #G
image_as_BGR_copy[:,:,2] = 0 #R
cv2.imshow("Imagen con solo el canal azul", image_as_BGR_copy)

image_as_BGR_copy = image_as_BGR.copy()
image_as_BGR_copy[:,:,0] = 0 #B
image_as_BGR_copy[:,:,2] = 0 #R
cv2.imshow("Imagen con solo el canal verde", image_as_BGR_copy)

image_as_BGR_copy = image_as_BGR.copy()
image_as_BGR_copy[:,:,0] = 0 #B
image_as_BGR_copy[:,:,1] = 0 #G
cv2.imshow("Imagen con solo el canal rojo", image_as_BGR_copy)

cv2.waitKey()
