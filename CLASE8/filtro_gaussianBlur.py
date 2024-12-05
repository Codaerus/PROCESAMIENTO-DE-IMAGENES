import cv2
import numpy as np 
help(cv2.GaussianBlur)
image = cv2.imread("mario.jpg")

kernel_size = (7,7)
sigma_X = 0 

#image_convoluted = cv2.medianBlur(image,kernel_size)
image_convoluted1 = cv2.blur(image,kernel_size,)
image_convoluted2 = cv2.GaussianBlur(image,kernel_size,sigma_X)
cv2.imshow("Imagen", image)
cv2.imshow("Promedio", image_convoluted1)
cv2.imshow("Gaussian", image_convoluted2)
cv2.waitKey()


#filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]]) -> dst
#GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) -> dst
"""
kernel = np.ones((5,5),np.float32)
width, height = kernel.shape
kernel /= (width*height)
"""
