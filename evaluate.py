# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_evaluate(object):
    def setupUi(self, evaluate):
        evaluate.setObjectName("evaluate")
        evaluate.resize(699, 509)
        self.centralwidget = QtWidgets.QWidget(evaluate)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 180, 521, 251))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.list1 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.list1.setObjectName("list1")
        self.horizontalLayout.addWidget(self.list1)
        self.list2 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.list2.setObjectName("list2")
        self.horizontalLayout.addWidget(self.list2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(100, 110, 501, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Players = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Players.setFont(font)
        self.Players.setAlignment(QtCore.Qt.AlignCenter)
        self.Players.setIndent(10)
        self.Players.setObjectName("Players")
        self.horizontalLayout_2.addWidget(self.Players)
        self.Points = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Points.setFont(font)
        self.Points.setAlignment(QtCore.Qt.AlignCenter)
        self.Points.setIndent(10)
        self.Points.setObjectName("Points")
        self.horizontalLayout_2.addWidget(self.Points)
        self.Calculate = QtWidgets.QPushButton(self.centralwidget)
        self.Calculate.setGeometry(QtCore.QRect(300, 440, 93, 28))
        self.Calculate.setObjectName("Calculate")
        self.SelectTeam = QtWidgets.QComboBox(self.centralwidget)
        self.SelectTeam.setGeometry(QtCore.QRect(150, 50, 141, 22))
        self.SelectTeam.setObjectName("SelectTeam")
        self.SelectMatch = QtWidgets.QComboBox(self.centralwidget)
        self.SelectMatch.setGeometry(QtCore.QRect(400, 50, 141, 22))
        self.SelectMatch.setObjectName("SelectMatch")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(60, 80, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        evaluate.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(evaluate)
        self.statusbar.setObjectName("statusbar")
        evaluate.setStatusBar(self.statusbar)
        self.SelectMatch.addItem("--SELECT MATCH--")
        self.SelectMatch.addItem("MATCH 1")
        self.SelectMatch.addItem("MATCH 2")
        self.SelectMatch.addItem("MATCH 3")
        self.SelectMatch.addItem("MATCH 4")
        self.SelectTeam.addItem("--SELECT TEAM--")
        self.SelectTeam.setDuplicatesEnabled(False)

        self.retranslateUi(evaluate)
        QtCore.QMetaObject.connectSlotsByName(evaluate)

    def retranslateUi(self, evaluate):
        _translate = QtCore.QCoreApplication.translate
        evaluate.setWindowTitle(_translate("evaluate", "MainWindow"))
        self.Players.setText(_translate("evaluate", "Players"))
        self.Points.setText(_translate("evaluate", "Points"))
        self.Calculate.setText(_translate("evaluate", "Calculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    evaluate = QtWidgets.QMainWindow()
    ui = Ui_evaluate()
    ui.setupUi(evaluate)
    evaluate.show()
    sys.exit(app.exec_())

