import cv2
import numpy as np 

cap=cv2.VideoCapture(0)

bajo = np.array([100,80,80]) #HSV
alto = np.array([126,255,255])
help(cv2.cvtColor)
while cap.isOpened():
    ret,frame=cap.read()
    frame_HSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    if ret == True:
        r_hsv = cv2.inRange(frame_HSV,bajo,alto)
        p = cv2.countNonZero(r_hsv)
        if p > 22000:
            text = "Objeto detectado"
            print(text)
        else:
            text = "Objeto no detectado"
            print(text)
        cv2.putText(frame, text, (20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.imshow("Mascara", r_hsv)
        cv2.imshow("Ventana", frame)
        val=cv2.waitKey(1)
        if val & 0xFF == ord("a"): 
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

#cvtColor(src, code[, dst[, dstCn]]) -> dst
