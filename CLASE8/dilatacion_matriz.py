import numpy as np 
import cv2

m = np.array([
			[255,255,0,0,0,255,255],
			[255,255,0,0,0,255,255],
			[255,255,0,0,0,255,255],
			[255,255,0,0,0,255,255],
			[255,255,0,0,0,255,255],
			[255,255,0,0,0,255,255],
			[255,255,0,0,0,255,255],
		],dtype=np.uint8)
#help(cv2.dilate)
print(m)
kernel = np.ones((3,3), np.uint8)
image_dilated = cv2.dilate(m,kernel)
print(image_dilated)
#erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) -> dst
#dilate(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) -> dst
