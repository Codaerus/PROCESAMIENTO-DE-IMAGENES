from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QFileDialog
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
		self.setGeometry(self.x, self.y, self.w, self.h)
		self.setWindowTitle(self.titulo)
		###################### BOTONES ######################
		boton = QPushButton("Cargar imagen", self)
		boton.setGeometry(60,50,100,40)
		boton.clicked.connect(self.loadImage)
		#####################################################
		self.label = QLabel(self)
		self.label.move(300,0)
		#####################################################
		self.show()
	def loadImage(self):
		file, _ = QFileDialog.getOpenFileName(self, "Selecionar imagen","","Imagenes (*.jpg *.png)")
		if file:
			path = file
			#Leer imagen
			print(path)
			image = cv2.imread(path)
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			#Convertir la imagen a unformato compatible con PyQt
			h,w,c = image.shape
			bytes_por_linea = c*w
			qimg = QImage(image.data,w, h,bytes_por_linea, QImage.Format_RGB888)
			#Mostrar la imagen
			pixmap = QPixmap.fromImage(qimg)
			self.label.setPixmap(pixmap)
			self.label.adjustSize()
app = QApplication([])
ex = App()
ex.initUI()
app.exec_()
