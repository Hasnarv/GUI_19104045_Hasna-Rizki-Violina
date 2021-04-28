import sys
from PyQt5.QtWidgets import QApplication

from HBoxLayout import *

if __name__ == '__main__':
	a = QApplication(sys.argv)

	form = HBoxLayout()
	form.show()

	a.exec_()