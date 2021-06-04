from PyQt5.QtWidgets import *

app = QApplication([])

# komponen untuk button Click
button = QPushButton('Click')

# fungsi ketika button di klik
def on_button_clicked():

    alert = QMessageBox()

    alert.setText('You clicked the button!')

    alert.exec_()

# untuk mengaktifkan button
button.clicked.connect(on_button_clicked)

button.show()

app.exec()