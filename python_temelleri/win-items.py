import sys
import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip,QWidget
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
   def __init__(self):
      super(MyWindow,self).__init__()
      self.setWindowTitle('First Application')
      self.setGeometry(200,200,500,300)
      self.setWindowIcon(QIcon('book.png'))
      self.setToolTip('My Tool')
      self.initUI()

   def clicked(self):
     print('You clicked to save button name '+self.txt_name.text() +' '+ self.txt_surname.text())   
 
   def initUI(self):
    self.lbl_name=QtWidgets.QLabel(self)
    self.lbl_name.setText('Name')
    self.lbl_name.move(50,30)

    self.lbl_surname=QtWidgets.QLabel(self)
    self.lbl_surname.setText('Surname')
    self.lbl_surname.move(50,80)

    self.txt_name = QtWidgets.QLineEdit(self)
    self.txt_name.move(100,30)
    
    self.txt_surname = QtWidgets.QLineEdit(self)
    self.txt_surname.move(100,80)

    self.btn_save= QtWidgets.QPushButton(self)
    self.btn_save.setText('Save')
    self.btn_save.move(100,130)
    self.btn_save.clicked.connect(self.clicked)


def window():
    app=QApplication(sys.argv)
    win=MyWindow()
    win.show()
    sys.exit(app.exec_())

window()