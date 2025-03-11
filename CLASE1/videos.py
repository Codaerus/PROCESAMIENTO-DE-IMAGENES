import cv2

#help(cv2.VideoCapture)

cap = cv2.VideoCapture(0)

while cap.isOpened():
	ret, frame = cap.read()
	if ret == True:
		cv2.imshow("Ventana",frame)
		val = cv2.waitKey(1)
		if val & 0xFF == ord("a"):
			break
		if val & 0xFF == ord("b"):
			cv2.imwrite("img1.jpg",frame)
	else:
		break
cap.release()
cv2.destroyAllWindows()

"""
isOpened(...)
 |      isOpened() -> retval
 |      .   @brief Returns true if video capturing has been initialized already.
read(...)
 |      read([, image]) -> retval, image
 |      .   @brief Grabs, decodes and returns the next video frame.
release(...)
 |      release() -> None
 |      .   @brief Closes video file or capturing device.

"""
