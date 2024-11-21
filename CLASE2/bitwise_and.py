import cv2
import numpy as np

m1 = np.array([
				[128,0],
			 	[255,255]
], dtype = np.uint8)

m2 = np.array([
				[128,0],
			 	[128,255]
], dtype = np.uint8)
AND = cv2.bitwise_and(m1,m2)
print(AND)

#help(cv2.bitwise_and)
#bitwise_and(src1, src2[, dst[, mask]])
