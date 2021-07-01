import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class DialogForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.resize(300, 100)
        self.move(320, 280)
        self.setWindowTitle('Dialog')
        self.label = QLabel('Form Kedua (Dialog)')
        self.okButton = QPushButton('OK')
        self.cancelButton = QPushButton('Batal')
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(hbox)
        self.setLayout(layout)
        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.resize(350, 100)
        self.move(300, 300)
        self.setWindowTitle('Demo QDialog.accept() danQDialog.reject()')
        self.label = QLabel('Form Utama')
        self.showDialogButton = QPushButton('Tampilkan Dialog')
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.showDialogButton)
        self.setLayout(layout)
        self.showDialogButton.clicked.connect(self.showDialogButtonClick)
    def showDialogButtonClick(self):
        form = DialogForm()
        if form.exec_() == QDialog.Accepted:
            QMessageBox.information(self, 'Informasi', 'Anda memilih tombol OK')
        else: # QDialog.Rejected
            QMessageBox.information(self, 'Informasi', 'Anda memilih tombol Batal')
if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()