import cv2
import numpy as np 

help(cv2.line)
z = np.zeros((400,400,3), dtype = np.uint8)
w,h,c = z.shape
print(w,h,c)
cv2.line(z,(0,0),(w-1,h-1),(0,255,0),4) #BGR
cv2.imshow("VENTANA", z)
cv2.waitKey(0)

#line(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
