import cv2
import numpy as np

help(cv2.imwrite)
z = cv2.imread("mario.jpg",0) #np.zeros((400,400), dtype = np.uint8)
print(z)
cv2.imshow("ventana",z)
cv2.waitKey(0)
cv2.imwrite("mario1.jpg",z)
#print(x)

#zeros(shape, dtype=float, order='C', *, like=None)->array
#imshow(winname, mat) -> None
#waitKey([, delay]) -> retval
#imread(filename[, flags]) -> retval
#imwrite(filename, img[, params]) -> retval
