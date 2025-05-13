import cv2
import matplotlib.pyplot as plt 

image_as_BGR = cv2.imread("image.png")
image_as_RGB = cv2.cvtColor(image_as_BGR,cv2.COLOR_BGR2RGB)
image_as_GRAY = cv2.cvtColor(image_as_BGR, cv2.COLOR_BGR2GRAY)

template_as_BGR = cv2.imread("plantilla.png")
template_as_GRAY = cv2.cvtColor(template_as_BGR,cv2.COLOR_BGR2GRAY)
h,w = template_as_GRAY.shape

method = cv2.TM_SQDIFF
result = cv2.matchTemplate(image_as_GRAY, template_as_GRAY, method)
min_value, max_value,min_cordinate, max_cordinate  = cv2.minMaxLoc(result)
print(min_value, max_value,min_cordinate, max_cordinate)

top_left = min_cordinate
bottom_right = min_cordinate[0]+w, min_cordinate[1]+h

cv2.rectangle(image_as_RGB,top_left, bottom_right, (0,255,0),2)
plt.imshow(image_as_RGB)
plt.show()
#cv2.matchTemplate( imagen, plantilla, método [ , resultado ] ) → resultado
