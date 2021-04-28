from PyQt5.QtWidgets import QWidget, QPushButton

class OtherForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()

	def setupUi(self):
		self.resize(400, 500)
		self.move(500, 500)
		self.setWindowTitle('Form Lain')

		self.button = QPushButton('Tutup')
		self.button.move(50, 50)
		self.button.setParent(self)

		self.button.clicked.connect(self.buttonClick)

	def buttonClick(self):
		self.close()