# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from new import Ui_new_2
from open import Ui_open
from score import Ui_score
from evaluate import Ui_evaluate
import sys
import sqlite3
Mymatch=sqlite3.connect('cricket.db')
cur=Mymatch.cursor()
global pointsused
global pointleft
class Ui_MainWindow(object):
    def __init__(self):
        self.newwindow=QtWidgets.QWidget()
        self.uinew=Ui_new_2()
        self.uinew.setupUi(self.newwindow)
        
        self.openwindow=QtWidgets.QWidget()
        self.uiopen=Ui_open()
        self.uiopen.setupUi(self.openwindow)
        
        self.evaluatewindow=QtWidgets.QMainWindow()
        self.uieval=Ui_evaluate()
        self.uieval.setupUi(self.evaluatewindow)
 
        self.scorewindow=QtWidgets.QMainWindow()
        self.uiscore=Ui_score()
        self.uiscore.setupUi(self.scorewindow)
               
 #open a new window  
    def opennew(self,action):
        txt= action.text()
        #open the new window
        if txt=='New Team':
            self.newwindow.show()
        #open the OPEN window
        elif txt=='Open Team':
            self.openwindow.show()
        #open the evaluate window
        elif txt=='Evaluate Team':
            self.evaluatewindow.show()
            
    def newteam(self):
        "this function sets the values of line edits after new team"
        a=self.uinew.t1.text()
        self.t7.setText(a)
        self.t1.setText("0")
        self.t2.setText("0")
        self.t3.setText("0")
        self.t4.setText("0")
        self.t6.setText("0")
        self.t5.setText("1000")
        self.list2.clear()
        self.newwindow.close()   
             
    def savewindow(self):
        "to save a team in the database"
        items=[]
        for index in range(self.list2.count()):
            items.append(self.list2.item(index).text())
        nm=self.uinew.t1.text()
        for i in range(len(items)):
            cur.execute("select score from stats where Player = '"+items[i]+"';")
            sr=cur.fetchone()
            cur.execute("insert into teams values (?,?,?);",(nm,items[i],sr[0]))
        Mymatch.commit()
        
    def evaluatewin(self):
        "when evalute window open"
        #self.savewindow()
        cur.execute("select Name from teams;")
        Team=cur.fetchall()
        teamlist=[]
        for i in range(len(Team)):
            teamlist.append(Team[i][0])
            
        for name in set(teamlist):
            self.uieval.SelectTeam.addItem(name)
            
    def evallist1(self):
        "evaluate the items of list1"
        nm=(self.uieval.SelectTeam.currentText())
        cur.execute("select Players from teams where Name='"+nm+"';")
        result=cur.fetchall()
        self.uieval.list1.clear()
        for i in range(0,len(result)):
            item=result[i][0]
            self.uieval.list1.addItem(item)  
        cur.execute("select Value from teams where Name = '"+nm+"';")
        score=cur.fetchall()
        self.uieval.list2.clear()
        for i in range(0,len(score)):
            item=score[i][0]
            self.uieval.list2.addItem(str(item))  
       
            
    def finalscore(self):
        "calculate the final score"
        nm=(self.uieval.SelectTeam.currentText())
        cur.execute("select Value from teams where Name = '"+nm+"';")
        score=cur.fetchall()
        teamscore=[]
        for i in range(len(score)):
            teamscore.append(score[i][0])
        self.scorewindow.show()
        a=(sum(teamscore))
        self.uiscore.Score.setText(str(a))
             
    def loadname(self):
        "load the names of the players in list1"
        if self.t1.text()=="##":
            self.message("Create a new team first")
        else:
            bat="BAT"
            bowl="BWl"
            wkt="WK"
            ar="AR"
            sql1="select Player from stats where ctg = '"+bat+"';"
            sql2="select Player from stats where ctg = '"+bowl+"';"
            sql3="select Player from stats where ctg = '"+ar+"';"
            sql4="select Player from stats where ctg = '"+wkt+"';"
            self.list1.clear()
            if self.rb2.isChecked()==True:
                cur.execute(sql2)
                for row in cur:
                    selected=[]
                    for i in range(self.list2.count()):
                        selected.append(self.list2.item(i).text())
                    if row[0] not in selected:
                        self.list1.addItem(row[0])
            
            if self.rb1.isChecked()==True:
                cur.execute(sql1)
                for row in cur:
                    selected=[]
                    for i in range(self.list2.count()):
                        selected.append(self.list2.item(i).text())
                    if row[0] not in selected:
                        self.list1.addItem(row[0])
            
            if self.rb3.isChecked()==True:
                cur.execute(sql3)
                for row in cur:
                    selected=[]
                    for i in range(self.list2.count()):
                        selected.append(self.list2.item(i).text())
                    if row[0] not in selected:
                        self.list1.addItem(row[0])
                    
            if self.rb4.isChecked()==True:
                cur.execute(sql4)
                for row in cur:
                    selected=[]
                    for i in range(self.list2.count()):
                        selected.append(self.list2.item(i).text())
                    if row[0] not in selected:
                        self.list1.addItem(row[0])
        
    def removelist1(self,item):
        "remove the selected players from list1"
        #self.list1.takeItem(self.list1.row(item))
        #self.list2.addItem(item.text())

        #to update the number of batsman
        if self.rb1.isChecked()==True:
            self.batcount+=1
            tst=self.error()
            if tst != False:
                self.list1.takeItem(self.list1.row(item))
                self.list2.addItem(item.text())
                self.t1.setText(str(self.batcount))
                self.totalpl+=1
            else:
                self.batcount-=1
        if self.rb2.isChecked()==True:
            self.bowlcount+=1
            tst=self.error()
            if tst != False:
                self.list1.takeItem(self.list1.row(item))
                self.list2.addItem(item.text())
                self.t2.setText(str(self.bowlcount))
                self.totalpl+=1
            else:
                self.bowlcount-=1
        if self.rb3.isChecked()==True:
            self.arcount+=1
            tst=self.error()
            if tst != False:
                self.list1.takeItem(self.list1.row(item))
                self.list2.addItem(item.text())
                self.t3.setText(str(self.arcount))
                self.totalpl+=1
            else:
                self.arcount-=1
        if self.rb4.isChecked()==True:
            self.wktcount+=1
            tst=self.error()
            if tst != False:
                self.list1.takeItem(self.list1.row(item))
                self.list2.addItem(item.text())
                self.t4.setText(str(self.wktcount))
                self.totalpl+=1   
            else:
                self.wktcount-=1
        cur.execute("select Value from stats where Player = '"+str(item.text())+"';")
        points=cur.fetchone()
        global pointsused
        global pointleft
        pointsused=int(pointsused)+int(points[0])
        if pointsused>=1000:
            global pointused
            self.message("You cannot use more than 1000 points")
            pointsused=int(pointsused)-int(points[0])
            
        self.t6.setText(str(pointsused))
        pointleft=1000-int(pointsused)
        self.t5.setText(str(pointleft))
        
        

    def removelist2(self,item):
        "remove the selected players from list1"
        self.list2.takeItem(self.list2.row(item))
        self.list1.addItem(item.text())
        #update the number of players 
        cur.execute("select ctg from stats where Player = '"+str(item.text())+"';")
        self.cat=cur.fetchone()
        
        if self.cat[0]=="BAT":
            self.batcount-=1
            self.t1.setText(str(self.batcount))
            self.totalpl-=1
        elif self.cat[0]=="BWl":
            self.bowlcount-=1
            self.t2.setText(str(self.bowlcount))
            self.totalpl-=1
        elif self.cat[0]=="AR":
            self.arcount-=1
            self.t3.setText(str(self.arcount))
            self.totalpl-=1
        elif self.cat[0]=="WKT":
            self.wktcount-=1
            self.t4.setText(str(self.wktcount))
            self.totalpl-=1
        cur.execute("select Value from stats where Player = '"+str(item.text())+"';")
        points=cur.fetchone()
        global pointsused
        global pointleft
        pointsused=int(pointsused)-int(points[0])
        self.t6.setText(str(pointsused))
        pointleft=1000-int(pointsused)
        self.t5.setText(str(pointleft))
    
    def message(self,x):
        "template for all message box"
        error_dialogue=QtWidgets.QErrorMessage()
        error_dialogue.showMessage(x)
        error_dialogue.exec_()
    
    def error(self):
        "function to handle all the exception"
        if self.totalpl>=12:
            self.message("You cannot select more than 11 players")
            a=self.list2.takeItem(11)
            self.list1.addItem(a.text())
        if self.wktcount==2:
            self.message("You can select only one wicket keeper")
            return False
        if self.batcount>=5:
            self.message("You can select only five batsmen")
            return False
        if self.bowlcount==5:
            self.message("You can select only five bowler")
            return False
        if self.arcount==3:
            self.message("You can select only three all rounder")
            return False
        
            
    
    def setupUi(self, MainWindow):
        #initializing variables
        self.batcount=0
        self.bowlcount=0
        self.arcount=0
        self.wktcount=0
        self.totalpl=0
        global pointsused
        pointsused=0
        global pointleft
        pointleft=1000
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.t1 = QtWidgets.QLineEdit(self.centralwidget)
        self.t1.setObjectName("t1")
        self.horizontalLayout_2.addWidget(self.t1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.t2 = QtWidgets.QLineEdit(self.centralwidget)
        self.t2.setObjectName("t2")
        self.horizontalLayout_2.addWidget(self.t2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.t3 = QtWidgets.QLineEdit(self.centralwidget)
        self.t3.setObjectName("t3")
        self.horizontalLayout_2.addWidget(self.t3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.t4 = QtWidgets.QLineEdit(self.centralwidget)
        self.t4.setObjectName("t4")
        self.horizontalLayout_2.addWidget(self.t4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.t5 = QtWidgets.QLineEdit(self.centralwidget)
        self.t5.setObjectName("t5")
        self.horizontalLayout_4.addWidget(self.t5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.t6 = QtWidgets.QLineEdit(self.centralwidget)
        self.t6.setObjectName("t6")
        self.horizontalLayout_4.addWidget(self.t6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rb1 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb1.setObjectName("rb1")
        self.horizontalLayout_3.addWidget(self.rb1)
        self.rb2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb2.setObjectName("rb2")
        self.horizontalLayout_3.addWidget(self.rb2)
        self.rb3 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb3.setObjectName("rb3")
        self.horizontalLayout_3.addWidget(self.rb3)
        self.rb4 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb4.setObjectName("rb4")
        self.horizontalLayout_3.addWidget(self.rb4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.t7 = QtWidgets.QLineEdit(self.centralwidget)
        self.t7.setObjectName("t7")
        self.horizontalLayout_3.addWidget(self.t7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.list1 = QtWidgets.QListWidget(self.centralwidget)
        self.list1.setObjectName("list1")
        self.horizontalLayout.addWidget(self.list1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.list2 = QtWidgets.QListWidget(self.centralwidget)
        self.list2.setObjectName("list2")
        self.horizontalLayout.addWidget(self.list2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addAction(self.actionOpen_Team)
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        #open window
        self.menuManage_Teams.triggered.connect(self.opennew)
        #new window
        self.uinew.pushButton.clicked.connect(self.newteam)
        
        #calling loadname                
        self.rb1.clicked.connect(self.loadname)   
        self.rb2.clicked.connect(self.loadname)
        self.rb3.clicked.connect(self.loadname)
        self.rb4.clicked.connect(self.loadname)
        
        #calling remove list     
        self.list1.itemDoubleClicked.connect(self.removelist1)  
        self.list2.itemDoubleClicked.connect(self.removelist2)
        
        self.actionSave_Team.triggered.connect(self.savewindow)
        #self.list2.itemEntered.connect(self.error)
        self.actionEvaluate_Team.triggered.connect(self.evaluatewin)
        #to fill the list widget of players
        self.uieval.SelectMatch.currentTextChanged.connect(self.evallist1)
        
        #calculate the finalscore
        self.uieval.Calculate.clicked.connect(self.finalscore)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.t1.setText(_translate("MainWindow", "##"))
        self.label_5.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.t2.setText(_translate("MainWindow", "##"))
        self.label_4.setText(_translate("MainWindow", "Allrounders(AR)"))
        self.t3.setText(_translate("MainWindow", "##"))
        self.label_3.setText(_translate("MainWindow", "Wicket-Keeper"))
        self.t4.setText(_translate("MainWindow", "##"))
        self.label.setText(_translate("MainWindow", "Points Available"))
        self.t5.setText(_translate("MainWindow", "####"))
        self.label_2.setText(_translate("MainWindow", "Points Used"))
        self.t6.setText(_translate("MainWindow", "####"))
        self.rb1.setText(_translate("MainWindow", "BAT"))
        self.rb2.setText(_translate("MainWindow", "BOW"))
        self.rb3.setText(_translate("MainWindow", "AR"))
        self.rb4.setText(_translate("MainWindow", "WK"))
        self.label_7.setText(_translate("MainWindow", "Team Name"))
        self.t7.setText(_translate("MainWindow", "Display here"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

