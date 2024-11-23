import cv2

help(cv2.cvtColor)

cap = cv2.VideoCapture(0)
azul1 = (100,100,50)
azul2 = (125,255,255)
while cap.isOpened():
	ret, frame = cap.read()
	frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(frame_hsv,azul1,azul2)
	AND = cv2.bitwise_and(frame,frame,mask=mask)
	if ret:
		cv2.imshow("ventana video", frame)
		#cv2.imshow("ventana2 video", frame_hsv)
		cv2.imshow("mascara", mask)
		cv2.imshow("AND", AND)
		val = cv2.waitKey(100)
		if val == 97: #La tela a
			break
	else:
		break
cap.release()
cv2.destroyAllWindows()
#cvtColor(src, code[, dst[, dstCn]]) -> dst
