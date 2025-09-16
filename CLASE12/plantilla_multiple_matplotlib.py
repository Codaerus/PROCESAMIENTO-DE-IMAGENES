import cv2
import matplotlib.pyplot as plt 
import numpy as np
image_as_BGR = cv2.imread("mario.png")
image_as_RGB = cv2.cvtColor(image_as_BGR, cv2.COLOR_BGR2RGB)
image_as_GRAY = cv2.cvtColor(image_as_BGR,cv2.COLOR_BGR2GRAY)

template_as_BGR = cv2.imread("blo.png")
template_as_GRAY = cv2.cvtColor(template_as_BGR, cv2.COLOR_BGR2GRAY)
h,w = template_as_GRAY.shape

method = cv2.TM_CCOEFF_NORMED
result = cv2.matchTemplate(image_as_GRAY, template_as_GRAY, method)
location = np.where(result>0.9)
location = location[::-1]
print(location)
for point in zip(*location):
	print(point)
	cv2.rectangle(image_as_RGB, point, (point[0]+w,point[1]+h),(0,0,255),2)

plt.figure(figsize=(15,5))
# Imagen original para la coincidencia
plt.subplot(1,3,1)
plt.imshow(image_as_RGB)
# Plantilla
plt.subplot(1,3,2)
plt.imshow(template_as_GRAY, cmap="gray")
# Mapa de calor del resultado
plt.subplot(1,3,3)
plt.imshow(result, cmap="gray")
plt.show()
