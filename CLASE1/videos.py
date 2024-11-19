import cv2

help(cv2.VideoCapture)

cap = cv2.VideoCapture(0)
while cap.isOpened():
	ret, frame = cap.read()
	if ret:
		cv2.imshow("ventana video", frame)
		val = cv2.waitKey(1)
		if val == 97:
			break
		if val == 98:
			cv2.imwrite("img1.jpg",frame)
	else:
		break
cap.release()
cv2.destroyAllWindows()


#isOpened() -> retval    Returns true if video capturing has been initialized already.
#read([, image]) -> retval, image  Decodes and returns the next video frame.
#release() -> None  Closes video file or capturing device.
