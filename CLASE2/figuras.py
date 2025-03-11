import cv2
import numpy as np 

help(cv2.putText)
z = np.zeros((200,400,3), dtype = np.uint8)
h,w,c = z.shape
#cv2.line(z,(0,0),(w-1,h-1),(0,255,0),4) #BGR
cv2.rectangle(z,(30,30),(370,170),(255,255,255),-1)
cv2.circle(z,(int(w/2),int(h/2)),60,(0,0,255),-1)
cv2.putText(z,"JAPON",(150,195),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255))
cv2.imshow("VENTANA", z)
cv2.waitKey(0)

#line(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
#rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
#circle(img, center, radius, color[, thickness[, lineType[, shift]]]) -> img
#putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) -> img
