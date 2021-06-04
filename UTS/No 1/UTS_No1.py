# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UTS_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from edit import*

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(486, 556)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 470, 311, 21))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Label Data Mahasiswa
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        # ListWidget untuk menampilkan data mahasiswa
        self.listWidget = QtWidgets.QListWidget(self.layoutWidget_2)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)

        # Label NIM
        self.labelNIM = QtWidgets.QLabel(self.layoutWidget_2)
        self.labelNIM.setObjectName("labelNIM")
        self.form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelNIM)

        # Label Nama
        self.labelNama = QtWidgets.QLabel(self.layoutWidget_2)
        self.labelNama.setObjectName("labelNama")
        self.form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelNama)

        # Label Jurusan
        self.labelJurusan = QtWidgets.QLabel(self.layoutWidget_2)
        self.labelJurusan.setObjectName("labelJurusan")
        self.form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelJurusan)

        # Label NoTelp
        self.labelNo = QtWidgets.QLabel(self.layoutWidget_2)
        self.labelNo.setObjectName("labelNo")
        self.form.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelNo)

        # Line Edit NIM
        self.lineNIM = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineNIM.setObjectName("lineNIM")
        self.form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineNIM)

        # Line Edit Nama
        self.lineNama = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineNama.setObjectName("lineNama")
        self.form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineNama)

        # Line Edit Jurusan
        self.lineJurusan = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineJurusan.setObjectName("lineJurusan")
        self.form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineJurusan)
        
        # Line Edit NoTelp
        self.lineNo = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineNo.setObjectName("lineNo")
        self.form.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineNo)

        # PushButton Tambah
        self.ButtonTambah = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonTambah.setObjectName("ButtonTambah")
        self.horizontalLayout.addWidget(self.ButtonTambah)
        self.ButtonTambah.clicked.connect(self.addButtonClick)

        # PushButton Edit
        self.ButtonEdit = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonEdit.setObjectName("ButtonEdit")
        self.horizontalLayout.addWidget(self.ButtonEdit)
        self.ButtonEdit.clicked.connect(self.editButtonClick)

        # PushButton Clear
        self.BUttonClear = QtWidgets.QPushButton(self.layoutWidget)
        self.BUttonClear.setDefault(False)
        self.BUttonClear.setFlat(False)
        self.BUttonClear.setObjectName("BUttonClear")
        self.horizontalLayout.addWidget(self.BUttonClear)
        self.BUttonClear.clicked.connect(self.listWidget.clear)

        # PushButton Hapus
        self.ButtonHapus = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonHapus.setObjectName("ButtonHapus")
        self.horizontalLayout.addWidget(self.ButtonHapus)
        self.ButtonHapus.clicked.connect(self.deleteButtonClick)

        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(17, 11, 450, 451))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        self.label.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"")
        
        
        self.form = QtWidgets.QFormLayout()
        self.form.setObjectName("form")
        self.verticalLayout.addLayout(self.form)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 486, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addButtonClick(self):
        self.listWidget.addItem(
            self.lineNIM.text() + ' - ' +
            self.lineNama.text() + ' - ' +
            self.lineJurusan.text() + ' - ' +
            self.lineNo.text())

    def editButtonClick(self):
        if self.listWidget.currentRow() < 0: return
        self.entryForm = EntryForm()
        s = str(self.listWidget.currentItem().text())
        idx = s.index('-')
        self.entryForm.nim.setText(s[:(idx-1)])
        self.entryForm.nama.setText(s[(idx-2):])
        self.entryForm.jurusan.setText(s[(idx-3):])
        self.entryForm.telp.setText(s[(idx-4):])

        if self.entryForm.exec_() == QDialog.Accepted:
            self.listWidget.currentItem().setText(
            self.entryForm.nim.text() + ' - ' +
            self.entryForm.nama.text() + ' - ' +
            self.entryForm.jurusan.text() + ' - ' +
            self.entryForm.telp.text())


    def deleteButtonClick(self):
        row = self.listWidget.currentRow()
        if row >= 0:
            self.listWidget.takeItem(row)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ButtonTambah.setText(_translate("MainWindow", "TAMBAH"))
        self.ButtonEdit.setText(_translate("MainWindow", "EDIT"))
        self.BUttonClear.setText(_translate("MainWindow", "CLEAR"))
        self.ButtonHapus.setText(_translate("MainWindow", "HAPUS"))
        self.label.setText(_translate("MainWindow", "Data Mahasiswa"))
        self.labelNIM.setText(_translate("MainWindow", "NIM"))
        self.labelNama.setText(_translate("MainWindow", "Nama"))
        self.labelJurusan.setText(_translate("MainWindow", "Jurusan"))
        self.labelNo.setText(_translate("MainWindow", "No.Telp"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())