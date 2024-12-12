import cv2

#help(cv2.Sobel)

img = cv2.imread("image.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
dx = 1
dy = 0
tamaño_kernel = 3
image_with_sobel = cv2.Sobel(img,cv2.CV_64F,dx,dy,tamaño_kernel)
cv2.imwrite("imagen_con_sobel.png",image_with_sobel)
cv2.imshow("ventana 1", img)
cv2.imshow("ventana 2", image_with_sobel)
cv2.waitKey(0)

#Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]]) -> dst
