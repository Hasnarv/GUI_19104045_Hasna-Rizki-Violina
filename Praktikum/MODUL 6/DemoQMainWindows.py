import sys, os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

PROGRAM_NAME = 'PyQt Editor'

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.currentFileName = ''
        self.setupUi()
    def setupUi(self):
        self.resize(550, 450)
        self.move(300, 300)
        self.setWindowTitle(PROGRAM_NAME + ' - Untitled')
        # inisialisasi teks pada statusbar
        self.statusBar().showMessage('Ketikkan teks yang Anda inginkan')
        # mendapatkan objek menubar
        menubar = self.menuBar()
        # membuat menu File dan menempatkannya ke dalam menubar
        fileMenu = menubar.addMenu('&File')
        # membuat aksi untuk menu File 
        fileNewAction = QAction(QIcon('icons/New.png'), 
        '&New', self)
        fileNewAction.setShortcut('Ctrl+N')
        fileNewAction.setStatusTip('Buat teks baru') 
        fileNewAction.triggered.connect(self.fileNewActionTriggered)
        fileMenu.addAction(fileNewAction) 
        fileOpenAction = QAction(QIcon('icons/Open.png'), 
        '&Open...', self)
        fileOpenAction.setShortcut('Ctrl+O')
        fileOpenAction.setStatusTip('Buka file')
        fileOpenAction.triggered.connect(self.fileOpenActionTriggered)
        fileMenu.addAction(fileOpenAction)
        fileMenu.addSeparator()
        fileSaveAction = QAction(QIcon('icons/Save.png'), 
        '&Save', self)
        fileSaveAction.setShortcut('Ctrl+S')
        fileSaveAction.setStatusTip('Simpan teks ke file')
        fileSaveAction.triggered.connect(self.fileSaveActionTriggered)
        fileMenu.addAction(fileSaveAction)
        fileSaveAsAction = QAction(QIcon(None), 'Save &As...', self)
        fileSaveAsAction.setStatusTip('Simpan teks ke file lain')
        fileSaveAsAction.triggered.connect(self.fileSaveAsActionTriggered)
        fileMenu.addAction(fileSaveAsAction)
        fileMenu.addSeparator()
        fileExitAction = QAction(QIcon(None), 'Exit', self)
        fileExitAction.setShortcut('Ctrl+Q')
        fileExitAction.setStatusTip('Buat dokumen baru')
        fileExitAction.triggered.connect(self.fileExitActionTriggered)
        fileMenu.addAction(fileExitAction)
        # membuat menu Edit dan menempatkannya ke dalam menubar
        editMenu = menubar.addMenu('&Edit')
        # membuat aksi untuk menu Edit
        editCutAction = QAction(QIcon('icons/Cut.png'), 
        'C&ut', self)
        editCutAction.setShortcut('Ctrl+X')
        editCutAction.setStatusTip('Potong teks')
        editCutAction.triggered.connect(self.editCutActionTriggered)
        editMenu.addAction(editCutAction) 
        editCopyAction = QAction(QIcon('icons/Copy.png'), 
        '&Copy', self)
        editCopyAction.setShortcut('Ctrl+C')
        editCopyAction.setStatusTip('Salin teks')
        editCopyAction.triggered.connect(self.editCopyActionTriggered)
        editMenu.addAction(editCopyAction)
        editMenu.addSeparator()
        editPasteAction = QAction(QIcon('icons/Paste.png'), 
        '&Paste', self)
        editPasteAction.setShortcut('Ctrl+V')
        editPasteAction.setStatusTip('Tempel teks (yang telah dipotong/disalin)')
        editPasteAction.triggered.connect(self.editPasteActionTriggered)
        editMenu.addAction(editPasteAction)
        # membuat menu Format dan menempatkannya ke dalam menubar
        formatMenu = menubar.addMenu('F&ormat')
        # membuat aksi untuk menu Format
        formatFontAction = QAction(QIcon(None), 'F&ont...', self)
        formatFontAction.setStatusTip('Menentukan jenis dan ukuran huruf pada teks yang disorot')
        formatFontAction.triggered.connect(self.formatFontActionTriggered)
        formatMenu.addAction(formatFontAction)
        # membuat toolbar
        toolbar = self.addToolBar('')
        toolbar.addAction(fileNewAction)
        toolbar.addAction(fileOpenAction)
        toolbar.addAction(fileSaveAction)
        toolbar.addSeparator()
        toolbar.addAction(editCutAction)
        toolbar.addAction(editCopyAction)
        toolbar.addAction(editPasteAction)
        # membuat objek QTextEdit dan menempatkannya ke dalam pusat widget
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
    def confirmation(self):
        if self.textEdit.document().isModified():
            response = QMessageBox.question(self, 
            'Konfirmasi',
            'Teks telah dimodifikasi. Simpan?')
            if response == QMessageBox.Yes:
                self.fileSaveActionTriggered()
    def fileNewActionTriggered(self):
        self.confirmation()
        self.textEdit.document().clear()
        self.currentFileName = ''
        self.setWindowTitle(PROGRAM_NAME + ' - Untitled')
    def fileOpenActionTriggered(self):
        self.confirmation()
        fileName = QFileDialog.getOpenFileName(self, 
        'Pilih file', os.curdir, 
        'File Teks (*.txt)',
        '*.txt')
        if not fileName[0]: return
        self.currentFileName = fileName[0]
        self.setWindowTitle(PROGRAM_NAME + ' - ' +
        self.currentFileName)
        fileHandle = QFile(fileName[0])
        if not fileHandle.open(QIODevice.ReadOnly): return
        stream = QTextStream(fileHandle)
        self.textEdit.setPlainText(stream.readAll())
        fileHandle.close()
    def writeToFile(self):
        fileHandle = QFile(self.currentFileName)
        if not fileHandle.open(QIODevice.WriteOnly): return
        stream = QTextStream(fileHandle)
        stream << self.textEdit.document().toPlainText()
        stream.flush() 
        fileHandle.close()
        self.textEdit.document().setModified(False)
    def fileSaveActionTriggered(self):
        if self.currentFileName == '':
            # mengeksekusi aksi Save As
            self.fileSaveAsActionTriggered()
        else:
            self.writeToFile()
    def fileSaveAsActionTriggered(self):
        fileName = QFileDialog.getSaveFileName(self, 
        'Simpan file', os.curdir, 
        'File Teks (*.txt)',
        '*.txt')
        if not fileName[0]: return
        self.currentFileName = fileName[0]
        self.setWindowTitle(PROGRAM_NAME + ' - ' + 
        self.currentFileName)
        self.writeToFile()
    def fileExitActionTriggered(self):
        sys.exit(0)
    def editCutActionTriggered(self):
        self.textEdit.cut()
    def editCopyActionTriggered(self):
         self.textEdit.copy()
    def editPasteActionTriggered(self):
        self.textEdit.paste()
    def formatFontActionTriggered(self):
        fontTuple = QFontDialog.getFont(
            QFont('Sans Serif', 11), 
            self, 'Pilih font')
        if fontTuple[0]:
            self.textEdit.setCurrentFont(fontTuple[0])


if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()








