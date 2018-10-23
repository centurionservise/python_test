# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pb_gui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(844, 638)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 30, 178, 29))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(730, 20, 47, 13))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 220, 87, 26))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuFggg = QtWidgets.QMenu(self.menubar)
        self.menuFggg.setObjectName("menuFggg")
        self.menuXxx = QtWidgets.QMenu(self.menubar)
        self.menuXxx.setObjectName("menuXxx")
        self.menuCcc = QtWidgets.QMenu(self.menubar)
        self.menuCcc.setObjectName("menuCcc")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionView_All = QtWidgets.QAction(MainWindow)
        self.actionView_All.setObjectName("actionView_All")
        self.actionRecords_Count = QtWidgets.QAction(MainWindow)
        self.actionRecords_Count.setObjectName("actionRecords_Count")
        self.menuFggg.addAction(self.actionOpen)
        self.menuFggg.addAction(self.actionSave)
        self.menuXxx.addAction(self.actionView_All)
        self.menuXxx.addAction(self.actionRecords_Count)
        self.menuCcc.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFggg.menuAction())
        self.menubar.addAction(self.menuXxx.menuAction())
        self.menubar.addAction(self.menuCcc.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Privat Bank API"))
        self.label_2.setText(_translate("MainWindow", "status"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menuFggg.setTitle(_translate("MainWindow", "File"))
        self.menuXxx.setTitle(_translate("MainWindow", "Data Base"))
        self.menuCcc.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionView_All.setText(_translate("MainWindow", "View All"))
        self.actionRecords_Count.setText(_translate("MainWindow", "Records Count"))

