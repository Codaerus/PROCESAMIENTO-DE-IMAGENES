import numpy as np 
import cv2

image_ad_BGR = cv2.imread("image_on_black_and_white.png")
image_ad_GRAY = cv2.cvtColor(image_ad_BGR,cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5), np.float32)

image_eroded = cv2.erode(image_ad_GRAY,kernel)

cv2.imshow("Imagen", image_ad_GRAY)
cv2.imshow("Imagen erosionada", image_eroded)
cv2.waitKey(0)

#erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) -> dst
