import cv2
import numpy as np
import matplotlib.pyplot as plt
help(cv2.calcHist)

image_as_BGR = cv2.imread("image_3.jpg")
image_as_GRAY = cv2.cvtColor(image_as_BGR, cv2.COLOR_BGR2GRAY)


histogram = cv2.calcHist([image_as_GRAY], [0], None, [255], [0,256])

cv2.imshow("imagen1",image_as_BGR)
plt.plot(histogram, color = "gray")
plt.show()
cv2.waitKey(0)
