import typing
from PyQt5 import QtCore, QtWidgets
import sys

from PyQt5.QtWidgets import QWidget
from MainWindow import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
      

      
      def __init__(self):
            super(myApp,self).__init__()
            self.ui=Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.btn_top.clicked.connect(self.calculate)
            self.ui.btn_cik.clicked.connect(self.calculate)
            self.ui.btn_carp.clicked.connect(self.calculate)
            self.ui.btn_bol.clicked.connect(self.calculate)

      def calculate(self):
       sender=self.sender().text()
       result=0

       if sender=='Addition':
        result=int(self.ui.txt_num01.text())+int(self.ui.txt_num02.text())
       elif sender=='Substraction':
        result=int(self.ui.txt_num01.text())-int(self.ui.txt_num02.text())
       elif sender=='Multiple':
        result=int(self.ui.txt_num01.text())*int(self.ui.txt_num02.text())
       elif sender=='Divide':
        result=int(self.ui.txt_num01.text())/int(self.ui.txt_num02.text())

       self.ui.lbl_result.setText('Result: '+str(result))    
        

def app():
   app=QtWidgets.QApplication(sys.argv)
   win=myApp()
   win.show()
   sys.exit(app.exec_())

app() 