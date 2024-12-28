import cv2
import numpy as np
help(cv2.calcHist)

image_as_BGR = cv2.imread("random_scene.jpg")
image_as_GRAY = cv2.cvtColor(image_as_BGR, cv2.COLOR_BGR2GRAY)

histogram = np.histogram(image_as_GRAY.ravel(),256,[0,255])
print(histogram)
cv2.imshow("imagen",image_as_BGR)
cv2.imshow("imagen_as_GRAY",image_as_GRAY)
cv2.waitKey(0)

#calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]]) -> hist
