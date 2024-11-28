import cv2
import numpy as np
help(cv2.getRotationMatrix2D)
image = cv2.imread("mario.jpg")

center = (0,0)
angle = 30
matrix_transformation = cv2.getRotationMatrix2D(center, angle, 1)
image_transformed = cv2.warpAffine(image, matrix_transformation, (400,400))
#print(matrix_transformation)

cv2.imshow("Imagen", image)
cv2.imshow("Imagen Transformada", image_transformed)
cv2.waitKey()

#getRotationMatrix2D(center, angle, scale) -> retval
#warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) -> dst
"""
Tx = 50
Ty = 50

matrix_transformation = np.float32([
										[1,0,Tx],
										[0,1,Ty]
									])
image_transformed = cv2.warpAffine(image, matrix_transformation, (400,400))
"""
