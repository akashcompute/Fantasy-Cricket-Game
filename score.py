# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'score.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_score(object):
    def setupUi(self, score):
        score.setObjectName("score")
        score.resize(471, 386)
        self.centralwidget = QtWidgets.QWidget(score)
        self.centralwidget.setObjectName("centralwidget")
        self.Score = QtWidgets.QLineEdit(self.centralwidget)
        self.Score.setGeometry(QtCore.QRect(180, 180, 113, 22))
        self.Score.setObjectName("Score")
        self.teamscore = QtWidgets.QLabel(self.centralwidget)
        self.teamscore.setGeometry(QtCore.QRect(180, 130, 151, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.teamscore.setFont(font)
        self.teamscore.setObjectName("teamscore")
        score.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(score)
        self.statusbar.setObjectName("statusbar")
        score.setStatusBar(self.statusbar)

        self.retranslateUi(score)
        QtCore.QMetaObject.connectSlotsByName(score)

    def retranslateUi(self, score):
        _translate = QtCore.QCoreApplication.translate
        score.setWindowTitle(_translate("score", "MainWindow"))
        self.teamscore.setText(_translate("score", "Your Team Score :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    score = QtWidgets.QMainWindow()
    ui = Ui_score()
    ui.setupUi(score)
    score.show()
    sys.exit(app.exec_())

