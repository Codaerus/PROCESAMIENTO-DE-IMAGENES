import cv2
import numpy as np 
#help(cv2.filter2D)
image = cv2.imread("mario.jpg")

kernel = np.ones((11,11),np.float32)
width, height = kernel.shape
kernel /= (width*height)

image_convoluted = cv2.filter2D(image, -1, kernel)

cv2.imshow("Imagen", image)
cv2.imshow("Imagen con la convolucion", image_convoluted)
cv2.waitKey()


#filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]]) -> dst
