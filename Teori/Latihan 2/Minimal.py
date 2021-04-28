import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

if __name__ == '__main__':
	a= QApplication(sys.argv)
	
	form = QWidget()
	form.resize(200,100)
	form.move(300,300)
	form.setWindowTitle('Ini adalah Form')
	
	label = QLabel('Pemrograman GUI')
	label.move(55,40)
	label.setParent(form)
	
	form.show()
	a.exec_()