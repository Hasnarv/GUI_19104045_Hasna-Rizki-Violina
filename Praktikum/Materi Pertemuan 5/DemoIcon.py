import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class DemoIcon(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.resize(400, 100)
        self.move(300, 300)
        self.setWindowTitle('Demo QPushButton')
        self.label = QLabel()
        self.label.setText('Demo QPushButton dengan gambar icon')
        icon1 = QIcon('add-icon.png')
        self.button1 = QPushButton('\tTambah')
        self.button1.setIcon(icon1)
        icon2 = QIcon('delete-icon.png')
        self.button2 = QPushButton('\tHapus')
        self.button2.setIcon(icon2)
        icon3 = QIcon('refresh-icon.png')
        self.button3 = QPushButton('\tRefresh')
        self.button3.setIcon(icon3)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(hbox)
        self.setLayout(layout)
if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = DemoIcon()
    form.show()
    a.exec_()