import cv2

#help(cv2.findContours)
image_as_BGR = cv2.imread("image_2.png")
image_as_GRAY = cv2.cvtColor(image_as_BGR,cv2.COLOR_BGR2GRAY)

valor_umbral = 127
valor_maximo = 255
tipo = cv2.THRESH_BINARY

ret, image_with_threshold = cv2.threshold(image_as_GRAY,valor_umbral,valor_maximo,tipo)
contours,hierarchy  = cv2.findContours(image_with_threshold, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
is_convex_contour = cv2.isContourConvex(contours[0])
print(is_convex_contour)
"""
perimetro = cv2.arcLength(contours[0],True)#cv2.contourArea(contours[0]) #cv2.moments(contours[0])
distance = 0.1*perimetro
approximate_contour = cv2.approxPolyDP(contours[0],distance,True)
"""
convex_hull = cv2.convexHull(contours[0])
cv2.drawContours(image_as_BGR,[convex_hull],-1,(0,0,255),2)
cv2.imshow("Imagen",image_as_BGR)
cv2.imshow("Imagen umbralizada", image_with_threshold)
cv2.waitKey()

print(contours)

#findContours(image, mode, method[, contours[, hierarchy[, offset]]]) -> contours, hierarchy
