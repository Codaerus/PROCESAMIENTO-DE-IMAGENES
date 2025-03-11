import cv2

#help(cv2.imread)
#help(cv2.imshow)
#help(cv2.waitKey)AAA
#imread(filename[, flags]) -> retval
#imshow(winname, mat) -> None
#waitKey([, delay]) -> retval
image = cv2.imread("mario.jpg",0)
cv2.imshow("IMAGEN DE MARIO", image)
cv2.waitKey()
#print(image, image.shape, image.ndim, image.dtype)
