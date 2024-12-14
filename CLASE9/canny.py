import cv2

help(cv2.Canny)
image_as_BGR = cv2.imread("image.png")
image_as_GRAY = cv2.cvtColor(image_as_BGR,cv2.COLOR_BGR2GRAY)
valor_umbral_min = 100
valor_umbral_max = 200
tamaño_kernel = 3
img_with_canny = cv2.Canny(image_as_GRAY,valor_umbral_min,valor_umbral_max,apertureSize = tamaño_kernel)

cv2.imshow("Imagen",image_as_BGR)
cv2.imshow("Imagen con Canny", img_with_canny)
cv2.waitKey()
#Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]]) -> edges
