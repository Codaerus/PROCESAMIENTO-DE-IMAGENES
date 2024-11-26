import cv2
import numpy
import matplotlib.pyplot as plt

#help(cv2.cvtColor)
image_as_BGR = cv2.imread("images.png")
#image_as_RGB = cv2.cvtColor(image_as_BGR,cv2.COLOR_BGR2RGB)
image_as_GRAY = cv2.cvtColor(image_as_BGR,cv2.COLOR_BGR2GRAY)

#cv2.imshow("Ventana BGR", image_as_BGR)
#cv2.imshow("Ventana RGB", image_as_RGB)
plt.title("Imagen como GRAY")
plt.imshow(image_as_GRAY,cmap=plt.get_cmap("gray"))
plt.yticks([])
plt.xticks([])
plt.show()
#cv2.waitKey()
#cvtColor(src, code[, dst[, dstCn]]) -> dst
