from PyQt5.QtWidgets import QWidget, QPushButton
from OtherForm import *

class MainForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()

	def setupUi(self):
		self.resize(400, 300)
		self.move(300, 300)
		self.setWindowTitle('Demo Menampilkan Form')

		self.button = QPushButton('Tampilkan Form Lain')
		self.button1 = QPushButton('Tutup')
		self.button.move(50, 50)
		self.button1.move(150, 150)
		self.button.setParent(self)
		self.button1.setParent(self)

		self.button.clicked.connect(self.buttonClick)
		self.button1.clicked.connect(self.buttonClick1)

	def buttonClick(self):
		self.form = OtherForm()
		self.form.show()

	def buttonClick1(self):
		self.close()