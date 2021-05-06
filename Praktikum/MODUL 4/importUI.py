from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(415, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 50, 181, 16))
        self.label.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.namaEdit = QtWidgets.QLineEdit(Form)
        self.namaEdit.setGeometry(QtCore.QRect(30, 80, 351, 21))
        self.namaEdit.setObjectName("namaEdit")
        self.hallo = QtWidgets.QPushButton(Form)
        self.hallo.setGeometry(QtCore.QRect(90, 130, 93, 28))
        self.hallo.setObjectName("hallo")
        self.Clear = QtWidgets.QPushButton(Form)
        self.Clear.setGeometry(QtCore.QRect(230, 130, 93, 28))
        self.Clear.setObjectName("Clear")
        self.Exit = QtWidgets.QPushButton(Form)
        self.Exit.setGeometry(QtCore.QRect(160, 170, 93, 28))
        self.Exit.setObjectName("Exit")

        self.retranslateUi(Form)
        self.Exit.clicked.connect(Form.close)
        self.Clear.clicked.connect(self.namaEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Masukkan Nama Anda :"))
        self.hallo.setText(_translate("Form", "Hallo"))
        self.Clear.setText(_translate("Form", "Clear"))
        self.Exit.setText(_translate("Form", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())