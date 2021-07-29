from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import pymysql.cursors

class Ui_datamhs(object):
    def setupUi(self, datamhs):
        datamhs.setObjectName("datamhs")
        datamhs.resize(508, 509)
        self.centralwidget = QtWidgets.QWidget(datamhs)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 511, 509))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("bg-data.png"))
        self.label.setObjectName("label")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 290, 461, 130))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 2, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 4, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 3, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 1, 0, 1, 1)
        
        self.onlyInt = QtGui.QIntValidator()    #validator biar cuma bisa diisi int
        self.onlyNo = QtGui.QRegExpValidator(QtCore.QRegExp("0[0-9]{11,13}"))  #validator biar cuma bisa diisi no.hp diawalin 0

        self.txtNIM_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtNIM_2.setObjectName("txtNIM_2")
        self.gridLayout_4.addWidget(self.txtNIM_2, 1, 2, 1, 1)
        self.txtNama_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        
        self.txtNama_2.setObjectName("txtNama_2")
        self.gridLayout_4.addWidget(self.txtNama_2, 2, 2, 1, 1)
        self.txtJurusan_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        
        self.txtJurusan_2.setObjectName("txtJurusan_2")
        self.gridLayout_4.addWidget(self.txtJurusan_2, 3, 2, 1, 1)
        self.txtNo_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        
        self.txtNo_2.setObjectName("txtNo_2")
        self.gridLayout_4.addWidget(self.txtNo_2, 4, 2, 1, 1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(120, 430, 371, 31))
        
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.btnTambah_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnTambah_2.setObjectName("btnTambah_2")
        self.btnTambah_2.clicked.connect(self.tambah_2)
        self.horizontalLayout_2.addWidget(self.btnTambah_2)
        
        self.btnEdit_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnEdit_2.setObjectName("btnEdit_2")
        self.btnEdit_2.clicked.connect(self.edit)
        self.horizontalLayout_2.addWidget(self.btnEdit_2)
        
        self.btnClear_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnClear_2.setObjectName("btnClear_2")
        self.btnClear_2.clicked.connect(self.clear_2)
        self.horizontalLayout_2.addWidget(self.btnClear_2)
        
        self.btnHapus_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnHapus_2.setObjectName("btnHapus_2")
        self.btnHapus_2.clicked.connect(self.hapus)
        self.horizontalLayout_2.addWidget(self.btnHapus_2)
        
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(30, 10, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        
        #table widget
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 70, 461, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(('NIM', 'Nama', 'Jurusan', 'No. Telp'))
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.itemClicked.connect(self.gett)
        self.baca()
        
        self.retranslateUi(datamhs)
        QtCore.QMetaObject.connectSlotsByName(datamhs)

    def retranslateUi(self, datamhs):
        _translate = QtCore.QCoreApplication.translate
        datamhs.setWindowTitle(_translate("datamhs", "MainWindow"))
        self.label_16.setText(_translate("datamhs", "Nama"))
        self.label_17.setText(_translate("datamhs", "No. Telp"))
        self.label_18.setText(_translate("datamhs", "Jurusan"))
        self.label_19.setText(_translate("datamhs", "NIM"))
        self.btnTambah_2.setText(_translate("datamhs", "Tambah"))
        self.btnEdit_2.setText(_translate("datamhs", "Edit"))
        self.btnClear_2.setText(_translate("datamhs", "Clear"))
        self.btnHapus_2.setText(_translate("datamhs", "Hapus"))
        self.label_15.setText(_translate("datamhs", "Data Mahasiswa"))


    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

        #fungsi read data
    def baca(self):
        con = pymysql.connect(db='db_mhs', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        result = cur.execute("SELECT * FROM mhs")
        self.tableWidget.setRowCount(0)
        
        for row_number, row_data in enumerate(cur):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        
        #fungsi select buat ngambil data   
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

        #fungsi untuk menambahkan data ke database
    def tambah_2(self):
        nim = self.txtNIM_2.text()
        nama = self.txtNama_2.text()
        jurusan = self.txtJurusan_2.text()
        no = self.txtNo_2.text()
        insert = (nim, nama, jurusan, no)
        print(insert)
        if self.txtNIM_2.text() and self.txtNama_2.text() and self.txtJurusan_2.text() and self.txtNo_2.text():
            con = pymysql.connect(db='db_mhs', user='root', passwd='', host='localhost', port=3306, autocommit=True)
            cur = con.cursor()
            sql = "INSERT INTO mhs(nim, nama, jurusan, no)" + "VALUES"+ str(insert)
            data = cur.execute(sql)
            self.messagebox("SUKSES", "Data Berhasil Ditambahkan")
            self.baca()
            self.clear_2()
        else:
            self.messagebox("GAGAL", "Mohon lengkapi form ")

        #fungsi edit di tab data
    def edit(self):
        nim = self.txtNIM_2.text()
        nama = self.txtNama_2.text()
        jurusan = self.txtJurusan_2.text()
        no = self.txtNo_2.text()
        con = pymysql.connect(db='db_mhs', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        sql = "UPDATE mhs SET nama=%s, jurusan=%s, no=%s WHERE nim=%s"
        data = cur.execute(sql, (nama, jurusan, no, nim))
        if (data):
            self.messagebox("SUKSES", "Data Mahasiswa Berhasil Di Edit")
        else:
            self.messagebox("GAGAL", "Data Mahasiswa Gagal Di Edit")
        self.baca()
        self.clear_2()

        #fungsi hapus di tab data
    def hapus(self):
        nim = self.txtNIM_2.text()
        con = pymysql.connect(db='db_mhs', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        sql = "DELETE FROM mhs where nim=%s"
        data = cur.execute(sql, (nim))
        if (data):
            self.messagebox("SUKSES", "Data Mahasiswa Berhasil Di Hapus")
        else:  
            self.messagebox("GAGAL", "Data Mahasiswa Gagal Di Hapus")
        self.baca()
        self.clear_2()

        #fungsi untuk menghapus lineedit stelah masukin data
    def clear_2(self):
        self.txtNIM_2.clear()
        self.txtNIM_2.setEnabled(True)
        self.txtNama_2.clear()
        self.txtJurusan_2.clear()
        self.txtNo_2.clear()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    datamhs = QtWidgets.QMainWindow()
    ui = Ui_datamhs()
    ui.setupUi(datamhs)
    datamhs.show()
    sys.exit(app.exec_())