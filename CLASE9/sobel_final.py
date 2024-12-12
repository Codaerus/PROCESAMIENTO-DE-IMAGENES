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
join_images = cv2.addWeighted(image_with_sobelx_abs,1,image_with_sobely_abs,1,0)

##################################################################
cv2.imshow("Vemtana1",img)
cv2.imshow("Ventana sobel",join_images)
cv2.waitKey(0)
