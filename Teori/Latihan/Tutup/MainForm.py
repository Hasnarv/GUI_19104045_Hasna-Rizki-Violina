from PyQt5.QtWidgets import QWidget, QPushButton

class MainForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()

	def setupUi(self):
		self.resize(400, 300)
		self.move(300, 300)
		self.setWindowTitle('Demo Menutup Form')

		self.button = QPushButton('Tutup')
		self.button.move(150, 150)
		self.button.setParent(self)

		self.button.clicked.connect(self.buttonClick)

	def buttonClick(self):
		self.close()