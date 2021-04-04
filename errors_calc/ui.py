from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(468, 318)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #f6d2ff")
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: #ffffff;\n"
"border: 2px solid #22222e;\n"
"border-radius: 10;\n"
"color: #000000")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(8, 5, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: #ffffff;\n"
"border: 2px solid #22222e;\n"
"border-radius: 10;\n"
"color: #000000")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 40, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: #22222e;\n"
"    background-color: #ffffff;\n"
"    border-radius: 8;\n"
"    border: 2px solid #000000;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:#d2d2d2;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(350, 70, 62, 22))
        self.doubleSpinBox.setAccelerated(True)
        self.doubleSpinBox.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.doubleSpinBox.setMinimum(1.0)
        self.doubleSpinBox.setMaximum(700.0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setProperty("value", 2.26)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 140, 466, 1))
        self.line.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(300, 0, 1, 140))
        self.line_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 190, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: #ffffff;\n"
"border: 2px solid #22222e;\n"
"border-radius: 10;\n"
"color: #000000")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(168, 190, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: #ffffff;\n"
"border: 2px solid #22222e;\n"
"border-radius: 10;\n"
"color: #000000")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(320, 190, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: #ffffff;\n"
"border: 2px solid #22222e;\n"
"border-radius: 10;\n"
"color: #000000")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 90, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color: #ffffff;\n"
"border: 2px solid #22222e;\n"
"border-radius: 10;\n"
"color: #000000")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(10, 270, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("background-color: #ffffff;\n"
"border: 2px solid #22222e;\n"
"border-radius: 10;\n"
"color: #000000")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(168, 270, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("background-color: #ffffff;\n"
"border: 2px solid #22222e;\n"
"border-radius: 10;\n"
"color: #000000")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(320, 270, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("background-color: #ffffff;\n"
"border: 2px solid #22222e;\n"
"border-radius: 10;\n"
"color: #000000")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 150, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 150, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(170, 230, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(320, 230, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 100, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    color: #22222e;\n"
"    background-color: #ffffff;\n"
"    border-radius: 8;\n"
"    border: 2px solid #000000;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:#d2d2d2;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TipaPlot"))
        self.pushButton.setText(_translate("MainWindow", "Add value"))
        self.label.setText(_translate("MainWindow", "Student coefficient"))
        self.label_2.setText(_translate("MainWindow", "Mean Value"))
        self.label_3.setText(_translate("MainWindow", "Variance"))
        self.label_4.setText(_translate("MainWindow", "Random Error"))
        self.label_5.setText(_translate("MainWindow", "Error (sys+ran)"))
        self.label_6.setText(_translate("MainWindow", "Square Variance"))
        self.label_7.setText(_translate("MainWindow", "Relative Error"))
        self.pushButton_2.setText(_translate("MainWindow", "Calculate!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
