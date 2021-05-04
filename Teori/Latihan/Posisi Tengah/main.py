import sys
from PyQt5.QtWidgets import QApplication

from PosisiTengah import *

if __name__ == '__main__':
	a = QApplication(sys.argv)

	form = PosisiTengah()
	form.show()

	a.exec_()