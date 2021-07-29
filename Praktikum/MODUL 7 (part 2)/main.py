from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import pymysql
import pymysql.cursors
from datamhs import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 509)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 551, 511))
        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(0, -110, 551, 581))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("bg.png"))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(170, 30, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 100, 421, 130))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 4, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 3, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 1, 0, 1, 1)
        
        self.onlyInt = QtGui.QIntValidator()    #validator biar cuma bisa diisi int
        self.onlyNo = QtGui.QRegExpValidator(QtCore.QRegExp("0[0-9]{11,13}"))  #validator biar cuma bisa diisi no.hp diawalin 0

        self.txtNIM = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtNIM.setObjectName("txtNIM")
        self.txtNIM.setValidator(self.onlyInt)              
        self.gridLayout_3.addWidget(self.txtNIM, 1, 2, 1, 1)

        self.txtNama = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtNama.setObjectName("txtNama")
        self.gridLayout_3.addWidget(self.txtNama, 2, 2, 1, 1)

        self.txtJurusan = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtJurusan.setObjectName("txtJurusan")
        self.gridLayout_3.addWidget(self.txtJurusan, 3, 2, 1, 1)

        self.txtNo = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtNo.setObjectName("txtNo")
        self.txtNo.setValidator(self.onlyNo)
        self.gridLayout_3.addWidget(self.txtNo, 4, 2, 1, 1)

        self.btnSubmit = QtWidgets.QPushButton(self.tab)
        self.btnSubmit.setGeometry(QtCore.QRect(390, 240, 88, 24))
        self.btnSubmit.setObjectName("btnSubmit")
        self.btnSubmit.clicked.connect(self.submit)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(-4, -8, 551, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("bg-data.png"))
        self.label.setObjectName("label")
        
        self.btnLogin = QtWidgets.QPushButton(self.tab_2)
        self.btnLogin.setGeometry(QtCore.QRect(370, 240, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.clicked.connect(self.login)

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(100, 140, 350, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        
        self.txtUname = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtUname.setObjectName("txtUname")
        self.gridLayout_2.addWidget(self.txtUname, 0, 1, 1, 1)
        
        self.txtPass = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtPass.setObjectName("txtPass")
        self.txtPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout_2.addWidget(self.txtPass, 1, 1, 1, 1)
        
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(200, 80, 170, 41))
        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Form Mahasiswa"))
        self.label_11.setText(_translate("MainWindow", "Nama"))
        self.label_12.setText(_translate("MainWindow", "No. Telp"))
        self.label_13.setText(_translate("MainWindow", "Jurusan"))
        self.label_14.setText(_translate("MainWindow", "NIM"))
        self.btnSubmit.setText(_translate("MainWindow", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Form"))
        self.btnLogin.setText(_translate("MainWindow", "LOGIN"))
        self.label_4.setText(_translate("MainWindow", "Username"))
        self.label_5.setText(_translate("MainWindow", "Password"))
        self.label_8.setText(_translate("MainWindow", "Login Admin"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Admin"))

    def koneksi(self):
        con = pymysql.connect(db='datamhs', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        #if(cur):
        #    self.messagebox("Koneksi", "Koneksi Berhasil")
        #else:
        #    self.messagebox("Koneksi", "Koneksi Gagal")

#fungsi untuk memunculkan dialog messagebox

    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

#fungsi read data

    #def baca(self):
    #    con = pymysql.connect(db='datamhs', user='root', passwd='', host='localhost', port=3306, autocommit=True)
    #    cur = con.cursor()
    #    result = cur.execute("SELECT * FROM mhs")
    #    self.tableWidget.setRowCount(0)
        
    #    for row_number, row_data in enumerate(cur):
    #        self.tableWidget.insertRow(row_number)
    #        for column_number, data in enumerate(row_data):
    #            self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        
#fungsi select untuk ngambil data   

    def gett(self):
        indexes = []
        for selectionRange in self.tableWidget.selectedRanges():
            indexes.extend(range(selectionRange.topRow(), selectionRange.bottomRow()+1))
        for i in indexes:
            self.txtNIM_2.setText(self.tableWidget.item(i, 0).text())
            self.txtNIM_2.setEnabled(False)
            self.txtNama_2.setText(self.tableWidget.item(i, 1).text())
            self.txtJurusan_2.setText(self.tableWidget.item(i, 2).text())
            self.txtNo_2.setText(self.tableWidget.item(i, 3).text())

#fungsi untuk menambahkan dari form ke db dan table widget

    def submit(self):
        nim = self.txtNIM.text()
        nama = self.txtNama.text()
        jurusan = self.txtJurusan.text()
        no = self.txtNo.text()
        insert = (nim, nama, jurusan, no)
        print(insert)
        if self.txtNIM.text() and self.txtNama.text() and self.txtJurusan.text() and self.txtNo.text():
            con = pymysql.connect(db='datamhs', user='root', passwd='', host='localhost', port=3306, autocommit=True)
            cur = con.cursor()
            sql = "INSERT INTO mhs(nim, nama, jurusan, no)" + "VALUES"+ str(insert)
            data = cur.execute(sql)
            self.messagebox("SUKSES", "Data Berhasil di Submit")
            #self.baca()
            self.clear()
        else:
            self.messagebox("GAGAL", "Mohon lengkapi form ")
      
    def login(self):
        uname = self.txtUname.text()
        pw = self.txtPass.text()
        con = pymysql.connect(db='datamhs', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        sql = "SELECT * from admin where uname=%s and pw=%s"
        data = cur.execute(sql, (uname, pw))
        if(len(cur.fetchall())>0):
            self.openadmin()
        else:
            self.messagebox("GAGAL", "Username atau Password Salah ! ")
        self.clearlogin()

    def openadmin(self):
        self.form = datamhs()
        self.form.show()


#fungsi untuk hapus lineedit stelah memasukan data

    def clear(self):
        self.txtNIM.clear()
        self.txtNIM.setEnabled(True)
        self.txtNama.clear()
        self.txtJurusan.clear()
        self.txtNo.clear()
    
    def clearlogin(self):
        self.txtUname.clear()
        self.txtPass.clear()


class datamhs(QWidget):
    def __init__(self):
        super().__init__()
        self.datamhs = Ui_datamhs()
        self.datamhs.setupUi(self)
        self.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())