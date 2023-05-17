
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon

def window():
    app=QApplication(sys.argv)
    win=QMainWindow()

    win.setWindowTitle('First Application')
    win.setGeometry(200,200,500,300)
    win.setWindowIcon(QIcon('book.png'))
    win.setToolTip('My Tool')

    win.show()
    sys.exit(app.exec_())

window()