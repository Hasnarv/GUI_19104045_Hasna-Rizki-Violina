from PyQt5.QtWidgets import QWidget, QLabel

class TextForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()

	def setupUi(self):
		self.resize(400, 200)
		self.move(300, 300)
		self.setWindowTitle('Demo Tag HTML')

		self.label1 = QLabel('<h1>Hello <font color=red>Afandi</font></h1>')
		self.label1.move(10, 10)
		self.label1.setParent(self)

		self.label2 = QLabel('''Teks ini dibuat dengan tag HTML. Teks dapat dijadikan <b>Tebal</b>
			<i>miring</i>, dan <u>Bergaris Bawah</i>''')
		self.label2.setWordWrap(True)
		self.label2.move(10,50)
		self.label2.setParent(self)