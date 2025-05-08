from PyQt5.QtWidgets import QWidget, QApplication, QLabel
import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.w = 600
		self.h = 300
		self.x = 100
		self.y = 100
		self.titulo = "PDI"
	def initUI(self):
		#####################################################
		#Leer imagen
		image = cv2.imread("mario.jpg")
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		#Convertir la imagen a unformato compatible con PyQt
		h,w,c = image.shape
		bytes_por_linea = c*w
		qimg = QImage(image,w, h,bytes_por_linea, QImage.Format_RGB888)
		#Mostrar la imagen
		pixmap = QPixmap(qimg)
		label = QLabel(self)
		label.setPixmap(pixmap)
		label.move(300,0)
		#####################################################
		self.setGeometry(self.x, self.y, self.w, self.h)
		self.setWindowTitle(self.titulo)
		self.show()

app = QApplication([])
ex = App()
ex.initUI()
app.exec_()
