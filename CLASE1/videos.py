import cv2

help(cv2.VideoCapture)

cap = cv2.VideoCapture(0)
while cap.isOpened():
	ret, frame = cap.read()
	if ret:
		cv2.imshow("ventana video", frame)
		if cv2.waitKey(1) == 97:
			break
	else:
		break
cap.release()
cv2.destroyAllWindows()


#isOpened() -> retval    Returns true if video capturing has been initialized already.
#read([, image]) -> retval, image  Decodes and returns the next video frame.
#release() -> None  Closes video file or capturing device.
