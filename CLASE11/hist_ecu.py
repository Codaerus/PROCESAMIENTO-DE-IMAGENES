import cv2
import numpy as np
import matplotlib.pyplot as plt



image_as_BGR = cv2.imread("image_3.jpg")
image_as_GRAY = cv2.cvtColor(image_as_BGR, cv2.COLOR_BGR2GRAY)


histogram, bins = np.histogram(image_as_GRAY.flatten(),256, [0,255])
histogram_cumulative_sum = histogram.cumsum()

histogram_cumulative_sum_masked = np.ma.masked_equal(histogram_cumulative_sum,0)
#Aplicamos la transformación de ecualización
histogram_cumulative_sum_masked = (histogram_cumulative_sum_masked - histogram_cumulative_sum_masked.min())*255/(histogram_cumulative_sum_masked.max() - histogram_cumulative_sum_masked.min())
#fill
histogram_cumulative_sum = np.ma.filled(histogram_cumulative_sum_masked,0).astype("uint8")
#Ecualizar la imagen
image = histogram_cumulative_sum[image_as_GRAY]

cv2.imshow("imagen1",image_as_BGR)
cv2.imshow("imagen2",image)
plt.plot(histogram, color = "b")
plt.hist(image.ravel(),255,[0,255],color = "gray")
plt.show()
cv2.waitKey(0)

