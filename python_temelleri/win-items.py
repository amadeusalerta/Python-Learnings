import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon

def window():
    app=QApplication(sys.argv)
    win=QMainWindow()

    def clicked(self):
     print('You clicked to save button name '+txt_name.text() +' '+ txt_surname.text())

    win.setWindowTitle('First Application')
    win.setGeometry(200,200,500,300)
    win.setWindowIcon(QIcon('book.png'))
    win.setToolTip('My Tool')

    lbl_name=QtWidgets.QLabel(win)
    lbl_name.setText('Name')
    lbl_name.move(50,30)

    lbl_surname=QtWidgets.QLabel(win)
    lbl_surname.setText('Surname')
    lbl_surname.move(50,80)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(100,30)
    
    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(100,80)

    btn_save= QtWidgets.QPushButton(win)
    btn_save.setText('Save')
    btn_save.move(100,130)
    btn_save.clicked.connect(clicked)


    win.show()
    sys.exit(app.exec_())

window()