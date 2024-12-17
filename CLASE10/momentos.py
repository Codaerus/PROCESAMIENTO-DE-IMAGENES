import cv2

help(cv2.findContours)
image_as_BGR = cv2.imread("image_2.png")
image_as_GRAY = cv2.cvtColor(image_as_BGR,cv2.COLOR_BGR2GRAY)

valor_umbral = 127
valor_maximo = 255
tipo = cv2.THRESH_BINARY

ret, image_with_threshold = cv2.threshold(image_as_GRAY,valor_umbral,valor_maximo,tipo)
contours,hierarchy  = cv2.findContours(image_with_threshold, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("Contornos")
print(contours)
moments = cv2.moments(contours[0])
print(moments)
cv2.drawContours(image_as_BGR,contours,-1,(255,0,0),2)
cv2.imshow("Imagen",image_as_BGR)
cv2.imshow("Imagen umbralizada", image_with_threshold)
cv2.waitKey()

print(contours)

#findContours(image, mode, method[, contours[, hierarchy[, offset]]]) -> contours, hierarchy
