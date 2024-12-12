import cv2
import matplotlib.pyplot as plt
#help(cv2.Sobel)

img = cv2.imread("image.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
########################## SOBEL X ###############################
dx = 1
dy = 0
tamaño_kernel = 3
image_with_sobelx = cv2.Sobel(img,cv2.CV_64F,dx,dy,tamaño_kernel)
image_with_sobelx_abs = cv2.convertScaleAbs(image_with_sobelx)
########################## SOBEL Y ###############################
dx = 0
dy = 1
tamaño_kernel = 3
image_with_sobely = cv2.Sobel(img,cv2.CV_64F,dx,dy,tamaño_kernel)
image_with_sobely_abs = cv2.convertScaleAbs(image_with_sobely)
##################################################################
join_images = cv2.addWeighted(image_with_sobelx,1,image_with_sobely,1,0)

##################################################################
plt.subplot(1,2,1)
plt.imshow(img,cmap="gray")

plt.subplot(1,2,2)
plt.imshow(join_images,cmap="gray")
plt.show()

"""
Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]]) -> dst
	Profundidad:  cv2.CV_64F | cv2.CV_8U | cv2.CV_16U | cv.CV_32S
				Representa el tipo de dato que utilizará el 
	dx: 1 y dy:0 -> significa que se calculará las derivadas en la dirección horizontal y la vertical se ignorará
	dx: 0 y dy:1 -> significa que se calculará las derivadas en la dirección vertical y la horizontal se ignorará
"""
