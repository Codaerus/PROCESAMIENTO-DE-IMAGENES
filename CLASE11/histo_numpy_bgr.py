import cv2
import matplotlib.pyplot as plt
help(cv2.calcHist)

image_as_BGR = cv2.imread("random_scene.jpg")
image_as_GRAY = cv2.cvtColor(image_as_BGR, cv2.COLOR_BGR2GRAY)

histogram_for_blue = cv2.calcHist([image_as_BGR],[0],None,[256],[0,256])
histogram_for_green = cv2.calcHist([image_as_BGR],[1],None,[256],[0,256])
histogram_for_red = cv2.calcHist([image_as_BGR],[2],None,[256],[0,256])

plt.plot(histogram_for_red, color = "r")
plt.plot(histogram_for_green, color = "g")
plt.plot(histogram_for_blue, color = "b")
plt.show()
cv2.imshow("imagen",image_as_BGR)
cv2.imshow("imagen_as_GRAY",image_as_GRAY)
cv2.waitKey(0)

#calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]]) -> hist
