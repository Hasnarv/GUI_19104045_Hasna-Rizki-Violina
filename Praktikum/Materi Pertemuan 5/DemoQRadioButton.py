import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.resize(400, 150)
        self.move(300, 300)
        self.setWindowTitle('Demo QRadioButton')
        self.label1 = QLabel()
        self.label1.setText('Siapa Dosen Pengampu Mata Kuliah <b>PemrogramanGUI</b>')
        self.cekCondro = QRadioButton()
        self.cekCondro.setText('&Condro Kartiko')
        self.cekCondro.setChecked(True)
        self.cekVanda = QRadioButton()
        self.cekVanda.setText('&Novanda Alim Setya')
        self.cekFandi = QRadioButton()
        self.cekFandi.setText('&Afandi Nur Aziz')
        self.cekGita = QRadioButton()
        self.cekGita.setText('&Gita Fadhila')
        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.cekCondro)
        vbox.addWidget(self.cekVanda)
        vbox.addWidget(self.cekFandi)
        vbox.addWidget(self.cekGita)
        self.resultLabel = QLabel('<b>Jawaban Anda: </b>')
        self.checkButton = QPushButton('Cek Jawaban')
        layout = QVBoxLayout()
        layout.addLayout(vbox)
        layout.addWidget(self.checkButton)
        layout.addWidget(self.resultLabel)
        layout.addStretch()
        self.setLayout(layout)
        self.checkButton.clicked.connect(self.checkButtonClick)
    def checkButtonClick(self):
        if self.cekFandi.isChecked():
            self.resultLabel.setText('<b>Jawaban Anda : Benar</b>')
        else:
            self.resultLabel.setText('<b>Jawaban Anda : Salah</b>')
if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()