import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.resize(450, 100)
        self.move(300, 300)
        self.setWindowTitle('Demo QMessageBox')
        self.aboutButton = QPushButton('About')
        self.criticalButton = QPushButton('Critical')
        self.informationButton = QPushButton('Information')
        self.questionButton = QPushButton('Question')
        self.warningButton = QPushButton('Warning')
        layout = QHBoxLayout()
        layout.addWidget(self.aboutButton)
        layout.addWidget(self.criticalButton)
        layout.addWidget(self.informationButton)
        layout.addWidget(self.questionButton)
        layout.addWidget(self.warningButton)
        self.setLayout(layout)
        self.aboutButton.clicked.connect(self.aboutButtonClick)
        self.criticalButton.clicked.connect(self.criticalButtonClick)
        self.informationButton.clicked.connect(self.informationButtonClick)
        self.questionButton.clicked.connect(self.questionButtonClick)
        self.warningButton.clicked.connect(self.warningButtonClick)
    def aboutButtonClick(self):
        QMessageBox.about(self, 'Tentang Program',
        'Video Recorder\n' +
        'Versi 1.0.0\n' +
        'Hak cipta (C) 2016 PyQt Lover Team')
    def criticalButtonClick(self):
        QMessageBox.critical(self, 'Kesalahan',
        'File settings.conf tidak ditemukan.')
    def informationButtonClick(self):
        QMessageBox.information(self, 'Informasi',
        'Proses upload file ke server telah berhasil dilakukan.')
    def questionButtonClick(self):
        fileName = 'settings.conf'
        response = QMessageBox.question(self, 'Konfirmasi', 'Anda yakin akan menghapus file %s?' % fileName)
        if response == QMessageBox.Yes:
            QMessageBox.about(self, 'Respon', 'Anda memilih tombol Yes')
        else:
            QMessageBox.about(self, 'Respon', 'Anda memilih tombol No')
    def warningButtonClick(self):
        QMessageBox.warning(self, 'Peringatan', 'Operasi ini akan menghapus semua data di dalam disk Anda!')
if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()