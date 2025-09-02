import cv2
import numpy as np 
import matplotlib.pyplot as plt 

image_as_BGR = cv2.imread("random_scene.jpg")

image_as_GRAY = cv2.cvtColor(image_as_BGR,cv2.COLOR_BGR2GRAY)
img_for_red = image_as_BGR[:,:,2]
img_for_green= image_as_BGR[:,:,1]
img_for_blue= image_as_BGR[:,:,0]
histogram_for_blue = cv2.calcHist([image_as_BGR],[0], None, [255],[0,256])
histogram_for_green = cv2.calcHist([image_as_BGR],[1], None, [255],[0,256])
histogram_for_red = cv2.calcHist([image_as_BGR],[2], None, [255],[0,256])

plt.plot(histogram_for_red, color = "r")
plt.plot(histogram_for_green, color = "g")
plt.plot(histogram_for_blue, color = "b")
cv2.imshow("image mario", image_as_BGR)
cv2.imshow("image mario canal rojo", img_for_red)
cv2.imshow("image mario canal green", img_for_green)
cv2.imshow("image mario canal blue", img_for_blue)
plt.show()
cv2.waitKey()

##histogram = cv2.calcHist([image_as_GRAY],[0], None, [255],[0,256])
