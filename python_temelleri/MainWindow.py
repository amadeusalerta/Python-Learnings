# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(725, 346)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 40, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 90, 51, 16))
        self.label_2.setObjectName("label_2")
        self.txt_num01 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_num01.setGeometry(QtCore.QRect(290, 40, 113, 20))
        self.txt_num01.setObjectName("txt_num01")
        self.txt_num02 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_num02.setGeometry(QtCore.QRect(290, 90, 113, 20))
        self.txt_num02.setObjectName("txt_num02")
        self.btn_top = QtWidgets.QPushButton(self.centralwidget)
        self.btn_top.setGeometry(QtCore.QRect(290, 130, 111, 41))
        self.btn_top.setObjectName("btn_top")
        self.btn_cik = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cik.setGeometry(QtCore.QRect(410, 130, 111, 41))
        self.btn_cik.setObjectName("btn_cik")
        self.btn_bol = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bol.setGeometry(QtCore.QRect(290, 180, 111, 41))
        self.btn_bol.setObjectName("btn_bol")
        self.btn_carp = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carp.setGeometry(QtCore.QRect(410, 180, 111, 41))
        self.btn_carp.setObjectName("btn_carp")
        self.lbl_result = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result.setGeometry(QtCore.QRect(290, 230, 111, 31))
        self.lbl_result.setObjectName("lbl_result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 725, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Number 1"))
        self.label_2.setText(_translate("MainWindow", "Number 2"))
        self.btn_top.setText(_translate("MainWindow", "Addition"))
        self.btn_cik.setText(_translate("MainWindow", "Substraction"))
        self.btn_bol.setText(_translate("MainWindow", "Multiple"))
        self.btn_carp.setText(_translate("MainWindow", "Divide"))
        self.lbl_result.setText(_translate("MainWindow", "Sonuç:"))
