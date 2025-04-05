import cv2

cap = cv2.VideoCapture(0)

kernel = 3
v_umbral_min = 100
v_umbral_max = 200

while cap.isOpened():
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	if ret == True:
		image_with_canny = cv2.Canny(gray, v_umbral_min, v_umbral_max, kernel)
		image_with_laplace = cv2.Laplacian(gray, cv2.CV_64F, ksize = 3)
		image_with_laplace = cv2.convertScaleAbs(image_with_laplace)
		cv2.imshow("Ventana",frame)
		cv2.imshow("Ventana Canny",image_with_canny)
		cv2.imshow("Ventana Laplace",image_with_laplace)
		val = cv2.waitKey(1)
		if val & 0xFF == ord("a"):
			break
	else:
		break
cap.release()
cv2.destroyAllWindows()
