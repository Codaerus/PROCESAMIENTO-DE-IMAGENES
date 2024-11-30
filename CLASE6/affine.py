import numpy as np
import cv2

image = cv2.imread("mario.jpg")
height, width, channels = image.shape

points_1 = np.float32([
						[50,50],
						[200,50],
						[50,200]
					])

points_2 = np.float32([
						[10,100],
						[200,20],
						[100,250]
					])

matrix_transformation = cv2.getAffineTransform(points_1,points_2)
image_transformed = cv2.warpAffine(image,matrix_transformation,(height, width))
for point in points_1:
	x,y = point
	point = tuple([ int(x), int(y)])
	cv2.circle(image,point,3,(0,255,0),-1)

for point in points_2:
	x,y = point
	point = tuple([ int(x), int(y)])
	cv2.circle(image_transformed,point,3,(0,0,255),-1)

cv2.imshow("Ventana",image)
cv2.imshow("Imagen Transformada",image_transformed)
cv2.waitKey()
