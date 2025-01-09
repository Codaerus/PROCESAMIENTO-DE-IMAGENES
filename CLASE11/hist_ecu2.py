import cv2
import numpy as np
import matplotlib.pyplot as plt

def eq_hist(image):
	histogram, bins = np.histogram(image.flatten(),256, [0,255])
	histogram_cumulative_sum = histogram.cumsum()

	histogram_cumulative_sum_masked = np.ma.masked_equal(histogram_cumulative_sum,0)
	#Aplicamos la transformación de ecualización
	histogram_cumulative_sum_masked = (histogram_cumulative_sum_masked - histogram_cumulative_sum_masked.min())*255/(histogram_cumulative_sum_masked.max() - histogram_cumulative_sum_masked.min())
	#fill
	histogram_cumulative_sum = np.ma.filled(histogram_cumulative_sum_masked,0).astype("uint8")
	#Ecualizar la imagen
	image = histogram_cumulative_sum[image]
	return image,histogram

image_as_BGR = cv2.imread("image5.jpg")

b,g,r = cv2.split(image_as_BGR)

image_b_equ,h1 = eq_hist(b)
image_g_equ,h2 = eq_hist(g)
image_r_equ,h3 = eq_hist(r)

image = cv2.merge((image_b_equ, image_g_equ, image_r_equ))

cv2.imshow("imagen1",image_as_BGR)
cv2.imshow("imagen2",image)
plt.plot(h1, color = "gray")
plt.plot(h2, color = "g")
plt.plot(h3, color = "r")
plt.hist(image.ravel(),255,[0,255],color = "b")
plt.show()
cv2.waitKey(0)
