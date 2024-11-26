import cv2
import numpy as np
#help(cv2.warpAffine)
image = cv2.imread("mario.jpg")

Tx = 50
Ty = 50

matrix_transformation = np.float32([
										[1,0,Tx],
										[0,1,Ty]
									])
image_transformed = cv2.warpAffine(image, matrix_transformation, (400,400))

cv2.imshow("Imagen", image)
cv2.imshow("Imagen Transformada", image_transformed)
cv2.waitKey()

#warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) -> dst
