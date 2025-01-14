import cv2
import matplotlib.pyplot as plt 

image_as_BGR = cv2.imread("image.png")
image_as_RGB = cv2.cvtColor(image_as_BGR,cv2.COLOR_BGR2RGB)
image_as_GRAY = cv2.cvtColor(image_as_BGR,cv2.COLOR_BGR2GRAY)

template_as_BGR = cv2.imread("plantilla.png")
template_as_GRAY = cv2.cvtColor(template_as_BGR,cv2.COLOR_BGR2GRAY)
h,w = template_as_GRAY.shape
print(h,w)
method = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_CCORR, cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]
method = method[1]
result = cv2.matchTemplate(image_as_GRAY,template_as_GRAY,method)
min_value,max_value,min_value_cordinate, max_value_cordinate = cv2.minMaxLoc(result)

if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
	top_left = min_value_cordinate
else:
	top_left = max_value_cordinate
print(top_left)
bottom_right = (top_left[0]  + 43 , top_left[1] + 43)
cv2.rectangle(image_as_RGB,top_left,bottom_right,(0,255,0),2)

plt.figure(figsize=(13,4))
plt.subplot(1,2,1)
plt.title("Resultado del emparejamiento")
plt.imshow(result,cmap = "gray")

plt.subplot(1,2,2)
plt.imshow(image_as_RGB)
plt.show()
