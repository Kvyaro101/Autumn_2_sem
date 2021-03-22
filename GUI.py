'''GUI and app'''

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtGui import QIcon

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

class Ui_MainWindow:
    '''GUI geometry'''
    def setupUi(self, MainWindow):
        '''Main GUI geometry'''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 567)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #dfb9e3\n"
" ")
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 20, 291, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:#f6f176;\n"
"border: 2px solid #fdbf00;\n"
"border-radius: 30px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("AB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setToolTip('#Best_Kirin')
        self.pushButton.setIconSize(QtCore.QSize(95, 95))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 130, 291, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:#c29ed6;\n"
"border: 2px solid #a864ce;\n"
"border-radius: 30px")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("TS.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setToolTip('''Alicorn with 'sparkling' cutiemark''')
        self.pushButton_2.setIconSize(QtCore.QSize(95, 95))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton_3.setGeometry(QtCore.QRect(50, 240, 291, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:#eeeef6;\n"
"border: 2px solid #c7c7c7;\n"
"border-radius: 30px")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("RT.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setToolTip('''Unicorn with 'gmph''')
        self.pushButton_3.setIconSize(QtCore.QSize(95, 95))
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 350, 291, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color:#e8cdf4;\n"
"border: 2px solid #ae85c1;\n"
"border-radius: 30px")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("StG.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setToolTip('''Unicorn with 'sparkling' cutiemark''')
        self.pushButton_4.setIconSize(QtCore.QSize(95, 95))
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 460, 291, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color:#a4d0ac;\n"
"border: 2px solid #39383a;\n"
"border-radius: 30px")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("EG.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setToolTip('Best Algebra Teacher')
        self.pushButton_5.setIconSize(QtCore.QSize(95, 95))
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        '''Buttons names'''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Autumn Blaze"))
        self.pushButton_2.setText(_translate("MainWindow", "Twilight Sparkle"))
        self.pushButton_3.setText(_translate("MainWindow", "Rarity"))
        self.pushButton_4.setText(_translate("MainWindow", "Starlight Glimmer"))
        self.pushButton_5.setText(_translate("MainWindow", "Goryachko"))

class mlp_bible(QtWidgets.QMainWindow):
    def __init__(self):
        '''GUI initiating'''
        super(mlp_bible, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        '''Actions initiated by clicking'''
        self.setWindowTitle ("Best Of MLP")
        self.setWindowIcon(QIcon('window_icon.jpg'))
        self.ui.pushButton.clicked.connect(self.PerformOperation)
        self.ui.pushButton_2.clicked.connect(self.PerformOperation_2)
        self.ui.pushButton_3.clicked.connect(self.PerformOperation_3)
        self.ui.pushButton_4.clicked.connect(self.PerformOperation_4)
        self.ui.pushButton_5.clicked.connect(self.PerformOperation_5)

    def PerformOperation(self):
        '''Initiating AB.wav'''
        filename = os.path.join(CURRENT_DIR, 'AB.wav')
        QtMultimedia.QSound.play(filename)
    def PerformOperation_2(self):
        '''Initiating TS.wav'''
        filename = os.path.join(CURRENT_DIR, 'TS.wav')
        QtMultimedia.QSound.play(filename)
    def PerformOperation_3(self):
        '''Initiating RT.wav'''
        filename = os.path.join(CURRENT_DIR, 'RT.wav')
        QtMultimedia.QSound.play(filename)
    def PerformOperation_4(self):
        '''Initiating StG.wav'''
        filename = os.path.join(CURRENT_DIR, 'StG.wav')
        QtMultimedia.QSound.play(filename)
    def PerformOperation_5(self):
        '''Initiating EG.wav'''
        filename = os.path.join(CURRENT_DIR, 'EG.wav')
        QtMultimedia.QSound.play(filename)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mlp_bible()
    application.show()
    sys.exit(app.exec_())
