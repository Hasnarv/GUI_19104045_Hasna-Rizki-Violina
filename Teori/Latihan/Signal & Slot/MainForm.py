from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton

class MainForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()

	def setupUi(self):
		self.resize(300, 100)
		self.move(300, 300)
		self.setWindowTitle('Demo Signal & Slot')

		self.lineEdit = QLineEdit()
		self.lineEdit.setText("Demo Signal dan Slot")

		self.button1 = QPushButton('Bersihkan')
		self.button2 = QPushButton('Tutup')

		hbox = QHBoxLayout()
		hbox.addWidget(self.button1)
		hbox.addWidget(self.button2)

		layout = QVBoxLayout()
		layout.addWidget(self.lineEdit)
		layout.addWidget(hbox)
		self.setLayout(layout)

		self.button1.clicked.connect(self.lineEdit.clear)
		self.button2.clicked.connect(self.close)