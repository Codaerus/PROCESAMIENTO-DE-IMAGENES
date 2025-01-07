import cv2
import numpy as np
import matplotlib.pyplot as plt
help(cv2.calcHist)

image_as_BGR = cv2.imread("random_scene.jpg")
image_as_GRAY = cv2.cvtColor(image_as_BGR, cv2.COLOR_BGR2GRAY)

mask = np.zeros(image_as_GRAY.shape, np.uint8)
mask[100:300,100:400] = 255

image_as_GRAY_with_mask = cv2.bitwise_and(image_as_GRAY,image_as_GRAY,mask = mask)
histogram = cv2.calcHist([image_as_GRAY], [0], mask, [255], [0,256])

cv2.imshow("imagen1",image_as_BGR)
cv2.imshow("imagen2",mask)
cv2.imshow("imagen2",image_as_GRAY_with_mask)
plt.plot(histogram, color = "gray")
plt.show()
cv2.waitKey(0)

#calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]]) -> hist
"""
						APLICANDO MÁSCARA
	Se crea una máscara para hacer énfasis a una región de la imágen, tal que la región tenga color blanco, mientras
	que el resto tenga color negro.
	Se hace uso de la función "calcHist", de OPENCV, para calcular el histograma
	El método "calcHist" recibe la máscara previamente creada
"""
