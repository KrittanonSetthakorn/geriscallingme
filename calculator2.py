

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(30, 10, 341, 91))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("%"))
        self.percentButton.setGeometry(QtCore.QRect(30, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.cButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("c"))
        self.cButton.setGeometry(QtCore.QRect(120, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.remove_it())
        self.arrowButton.setGeometry(QtCore.QRect(210, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(300, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(30, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(30, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(30, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.plusminus_it())
        self.plusminusButton.setGeometry(QtCore.QRect(30, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setObjectName("plusminusButton")
        self.eightButtton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("8"))
        self.eightButtton.setGeometry(QtCore.QRect(120, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButtton.setFont(font)
        self.eightButtton.setObjectName("eightButtton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(120, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(120, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(120, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(210, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(210, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(210, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.dot_it())
        self.decimalButton.setGeometry(QtCore.QRect(210, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("x"))
        self.multiplyButton.setGeometry(QtCore.QRect(300, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(300, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.plusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("+"))
        self.plusButton.setGeometry(QtCore.QRect(300, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.math_it())
        self.equalButton.setGeometry(QtCore.QRect(300, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def remove_it(self):
         screen = self.outputLabel.text()
         screen = screen[:-1]
         self.outputLabel.setText(screen)
        
    def math_it(self):
        screen = self.outputLabel.text() 
        try:
            answer =  eval(screen)
            self.outputLabel.setText(str(answer))
        except:
            self.outputLabel.setText("ERROR")

    def plusminus_it(self):
        screen = self.outputLabel.text()
        if "-" in screen:
            self.outputLabel.setText(screen.replace("-", ""))
        else:
            self.outputLabel.setText(f' -{screen}')


    def dot_it(self):
        screen = self.outputLabel.text()

        if screen[-1] == ".":
            pass
        else:
            self.outputLabel.setText(f' {screen}.')

    def press_it(self, pressed):
        if pressed == "c":
            self.outputLabel.setText("0")
        else:
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.cButton.setText(_translate("MainWindow", "c"))
        self.arrowButton.setText(_translate("MainWindow", "<"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))
        self.eightButtton.setText(_translate("MainWindow", "8"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.equalButton.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
