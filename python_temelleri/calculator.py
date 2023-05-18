import sys
import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

class MainForm(QMainWindow):
   def __init__(self):
      super(MainForm,self).__init__()

      self.setWindowTitle('Calculator')
      self.setGeometry(300,300,500,500)
      self.initUI()
    
   def initUI(self):
      self.lbl_num01=QtWidgets.QLabel(self)
      self.lbl_num01.setText('Number 1:')
      self.lbl_num01.move(50,30)

      self.txt_num01=QtWidgets.QLineEdit(self)
      self.txt_num01.move(150,30)
      self.txt_num01.resize(200,32)

      self.lbl_num02=QtWidgets.QLabel(self)
      self.lbl_num02.setText('Number 2:')
      self.lbl_num02.move(50,80)

      self.txt_num02=QtWidgets.QLineEdit(self)
      self.txt_num02.move(150,80)
      self.txt_num02.resize(200,32)

      self.bttn_topla=QtWidgets.QPushButton(self)
      self.bttn_topla.setText('Addition')
      self.bttn_topla.move(150,130)
      self.bttn_topla.clicked.connect(self.calculate)

      self.bttn_cikar=QtWidgets.QPushButton(self)
      self.bttn_cikar.setText('Substraction')
      self.bttn_cikar.move(150,180)
      self.bttn_cikar.clicked.connect(self.calculate)

      self.bttn_carp=QtWidgets.QPushButton(self)
      self.bttn_carp.setText('Multiple')
      self.bttn_carp.move(250,130)
      self.bttn_carp.clicked.connect(self.calculate)

      self.bttn_bol=QtWidgets.QPushButton(self)
      self.bttn_bol.setText('Divide')
      self.bttn_bol.move(250,180)
      self.bttn_bol.clicked.connect(self.calculate)

      self.lbl_result=QtWidgets.QLabel(self)
      self.lbl_result.setText('Result:')
      self.lbl_result.move(150,230)
   
   def calculate(self):
      sender=self.sender().text()
      result=0

      if sender=='Addition':
       result=int(self.txt_num01.text())+int(self.txt_num02.text())
      elif sender=='Substraction':
       result=int(self.txt_num01.text())-int(self.txt_num02.text())
      elif sender=='Multiple':
       result=int(self.txt_num01.text())*int(self.txt_num02.text())
      elif sender=='Divide':
       result=int(self.txt_num01.text())/int(self.txt_num02.text())

      self.lbl_result.setText('Result: '+str(result))

   # def toplama(self):
   #    result=int(self.txt_num01.text())+int(self.txt_num02.text())
   #    self.lbl_result.setText('Result: '+str(result))
   
   # def cikarma(self):
   #    result=int(self.txt_num01.text())-int(self.txt_num02.text())
   #    self.lbl_result.setText('Result: '+str(result))

   # def carpma(self):
   #    result=int(self.txt_num01.text())*int(self.txt_num02.text())
   #    self.lbl_result.setText('Result: '+str(result))

   # def bolme(self):
   #    result=int(self.txt_num01.text())/int(self.txt_num02.text())
   #    self.lbl_result.setText('Result: '+str(result))
   



def app():
   app=QApplication(sys.argv)
   win=MainForm()
   win.show()
   sys.exit(app.exec_())

app()   

