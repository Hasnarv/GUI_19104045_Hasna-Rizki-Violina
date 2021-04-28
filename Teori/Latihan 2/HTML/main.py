import sys
from PyQt5.QtWidgets import QApplication

from TextForm import *

if __name__ == '__main__':
	a = QApplication(sys.argv)

	form = TextForm()
	form.show()
	a.exec_()