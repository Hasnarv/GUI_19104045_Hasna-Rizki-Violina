from PyQt5.QtWidgets import QWidget, QLabel

class MinimalForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()

	def setupUi(self):
		self.resize(500, 200)
		self.move(400, 400)
		self.setWindowTitle('GUI Minimal')

		self.label = QLabel('Hello Gaes')
		self.label.move(100, 40)
		self.label.setParent(self)