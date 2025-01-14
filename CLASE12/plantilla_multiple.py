import cv2
import matplotlib.pyplot as plt 
import numpy as np

image_as_BGR = cv2.imread("mario.png")
image_as_RGB = cv2.cvtColor(image_as_BGR,cv2.COLOR_BGR2RGB)
image_as_GRAY = cv2.cvtColor(image_as_BGR,cv2.COLOR_BGR2GRAY)

template_as_BGR = cv2.imread("blo.png")
template_as_GRAY = cv2.cvtColor(template_as_BGR,cv2.COLOR_BGR2GRAY)
h,w = template_as_GRAY.shape
#print(h,w)
method = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_CCORR, cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]
method = method[1]
result = cv2.matchTemplate(image_as_GRAY,template_as_GRAY,method)

valor_umbral = 0.97
location = np.where(result>=valor_umbral)
location = location[::-1]
#print(location)

for point in zip(*location):
	print(point)
	cv2.rectangle(image_as_BGR,point,(point[0]+w,point[1]+h),(0,0,255),2)
	#cv2.circle(image_as_BGR,point,30,(0,255,0),2)

cv2.imshow("Imagen con los objetos encontrados",image_as_BGR)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

print(list(zip([14, 14, 14, 14, 14],[ 69,  99, 190, 281, 311])))

import numpy as np 

arr = np.array([10,20,30,40,50])
i = np.where(arr>25)
print(i)
"""
