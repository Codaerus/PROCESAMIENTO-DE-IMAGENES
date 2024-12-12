import cv2
import matplotlib.pyplot as plt
#help(cv2.Sobel)

img = cv2.imread("image.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
########################## SOBEL X ###############################
dx = 1
dy = 0
image_with_Scharrx = cv2.Scharr(img,cv2.CV_64F,dx,dy)
image_with_Scharrx_abs = cv2.convertScaleAbs(image_with_Scharrx)
########################## SOBEL Y ###############################
dx = 0
dy = 1
image_with_Scharry = cv2.Scharr(img,cv2.CV_64F,dx,dy)
image_with_Scharry_abs = cv2.convertScaleAbs(image_with_Scharry)
##################################################################
join_images = cv2.addWeighted(image_with_Scharrx_abs,1,image_with_Scharry_abs,1,0)

##################################################################
cv2.imshow("Vemtana1",img)
cv2.imshow("Ventana Scharr",join_images)
cv2.waitKey(0)

"""
Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]]) -> dst
	Profundidad:  cv2.CV_64F | cv2.CV_8U | cv2.CV_16U | cv.CV_32S
				Representa el tipo de dato que utilizará el 
	dx: 1 y dy:0 -> significa que se calculará las derivadas en la dirección horizontal y la vertical se ignorará
	dx: 0 y dy:1 -> significa que se calculará las derivadas en la dirección vertical y la horizontal se ignorará
"""
