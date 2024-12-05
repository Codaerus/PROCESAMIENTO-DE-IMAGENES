import cv2
import numpy as np 
#help(cv2.filter2D)
image = cv2.imread("image_with_noise_salt_and_pepper.png")


kernel_size = 3
image_convoluted = cv2.medianBlur(image,kernel_size)

cv2.imshow("Imagen", image)
cv2.imshow("Imagen con la convolucion", image_convoluted)
cv2.waitKey()


#filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]]) -> dst

"""
kernel = np.ones((5,5),np.float32)
width, height = kernel.shape
kernel /= (width*height)
"""
