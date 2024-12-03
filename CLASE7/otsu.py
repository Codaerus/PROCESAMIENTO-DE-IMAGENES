import numpy as np
import cv2
import matplotlib.pyplot as plt 

image_as_BGR = cv2.imread("image_with_noise.png")
image_as_GRAY = cv2.cvtColor(image_as_BGR, cv2.COLOR_BGR2GRAY)
#help(cv2.calcHist)
image_as_GRAY = cv2.GaussianBlur(image_as_GRAY,(7,9),27)
valor_maximo = 255
valor_umbral = 100
tipo = cv2.THRESH_BINARY + cv2.THRESH_OTSU
#print(cv2.THRESH_BINARY_INV,cv2.THRESH_OTSU)
ret_value, image_with_THRESH_BINARY_and_OUTSU = cv2.threshold(image_as_GRAY,valor_umbral,valor_maximo,tipo)
histogram_for_gray = cv2.calcHist([image_as_GRAY],[0],None,[256],[0,256])

cv2.imshow("Ventana",image_as_GRAY)
cv2.imshow("Imagen con la umbralización",image_with_THRESH_BINARY_and_OUTSU)

plt.plot(histogram_for_gray, color="gray")
plt.show()
cv2.waitKey()

#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]]) -> hist
