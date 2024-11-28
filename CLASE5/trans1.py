from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 

image = Image.open("mario.jpg")
width, height = image.size
#print(image.size)
#######################    ESCALAMIENTO    #################################
Sx = 2
Sy = 2

matrix_transformation_1 = np.float32([
										[Sx,  0,  0],
										[0,  Sx,  0],
										[0,   0,  1]
									])
#####################    TRASLACIÓN    #####################################
Tx = 50
Ty = 70

matrix_transformation_2 =  np.float32([
										[1,   0,  Tx],
										[0,   1,  Ty],
										[0,   0,   1]
									])
############################################################################
composition = matrix_transformation_1@matrix_transformation_2

composition_inverse = np.linalg.inv(composition)
composition_inverse = composition_inverse[:-1]

output_size = (int(Sx*width), int(Sy*height))
image_transformed = image.transform(output_size,Image.AFFINE,data = composition_inverse.flatten())

plt.title("Imagen transformada")
plt.imshow(np.array(image_transformed))
plt.show()
#transform(size, method, data=None) -> 'Image'
