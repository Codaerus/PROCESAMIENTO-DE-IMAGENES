import numpy as np
import cv2

image = cv2.imread("sudoku.jpg")
height, width, channels = image.shape

points_1 = np.float32([
						[56,65],
						[368,52],
						[28,387],
						[389,390]
					])

points_2 = np.float32([
						[0,0],
						[300,0],
						[0,300],
						[300,300]
					])

matrix_transformation = cv2.getPerspectiveTransform(points_1,points_2)
image_transformed = cv2.warpPerspective(image,matrix_transformation,(300,300))
for point in points_1:
	x,y = point
	point = tuple([ int(x), int(y)])
	cv2.circle(image,point,5,(0,255,0),-1)

for point in points_2:
	x,y = point
	point = tuple([ int(x), int(y)])
	cv2.circle(image,point,5,(0,0,255),-1)

cv2.imshow("Ventana",image)
cv2.imshow("Imagen Transformada",image_transformed)
cv2.waitKey()
