import numpy as np 
import cv2

m = np.array([
			[255,255,255,0,255,255,255],
			[255,255,255,0,255,255,255],
			[255,255,255,0,255,255,255],
			[255,255,255,0,255,255,255],
			[255,255,255,0,255,255,255],
			[255,255,255,0,255,255,255],
			[255,255,255,0,255,255,255],
		],dtype=np.uint8)

print(m)
kernel = np.ones((3,3), np.uint8)
image_eroded = cv2.erode(m,kernel)
image_eroded = cv2.erode(image_eroded,kernel)
print(image_eroded)
#erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) -> dst
