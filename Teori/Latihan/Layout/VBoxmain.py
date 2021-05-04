import sys
from PyQt5.QtWidgets import QApplication

from VBoxLayout import *

if __name__ == '__main__':
	a = QApplication(sys.argv)

	form = VBoxLayout()
	form.show()

	a.exec_()