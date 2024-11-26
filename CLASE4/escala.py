import cv2
import numpy
#help(cv2.resize)
image = cv2.imread("mario.jpg")

Sx = 1.2 
Sy = 1.5
image_transformed = cv2.resize(image,None,fx = Sx , fy = Sy)

cv2.imshow("Imagen", image)
cv2.imshow("Imagen Transformada", image_transformed)
cv2.waitKey()


#resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]) -> dst
