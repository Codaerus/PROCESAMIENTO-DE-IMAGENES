from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QFileDialog, QComboBox
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
		#################### LABEL ######################
		self.label = QLabel(self)
		self.label.move(300,0)
		################### QComboBox ######################
		self.formatC = QComboBox(self)
		self.formatC.addItem("RGB")
		self.formatC.addItem("BGR")
		self.formatC.currentIndexChanged.connect(self.setFormat)
		self.formatC.move(60,100)
		#####################################################
		self.show()
	def setFormat(self):
		if self.image is not None:
			selector = self.formatC.currentText()
			if selector == "RGB":
				self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
			if selector == "BGR":
				self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
			self.displayImage(self.image)

	def displayImage(self,image):
		#Convertir la imagen a unformato compatible con PyQt
			h,w,c = image.shape
			bytes_por_linea = c*w
			qimg = QImage(self.image.data,w, h,bytes_por_linea, QImage.Format_RGB888)
			#Mostrar la imagen
			pixmap = QPixmap.fromImage(qimg)
			self.label.setPixmap(pixmap)
			self.label.adjustSize()
	def loadImage(self):
		file, _ = QFileDialog.getOpenFileName(self, "Selecionar imagen","","Imagenes (*.jpg *.png)")
		if file:
			path = file
			#Leer imagen
			print(path)
			self.image = cv2.imread(path)
			self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
			self.displayImage(self.image)

app = QApplication([])
ex = App()
ex.initUI()
app.exec_()
