# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pb_gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(535, 440)
        self.label_period_start = QtWidgets.QLabel(Form)
        self.label_period_start.setGeometry(QtCore.QRect(20, 50, 78, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_period_start.setFont(font)
        self.label_period_start.setObjectName("label_period_start")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 110, 152, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lcdNumber = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 170, 481, 254))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_request = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_request.setObjectName("btn_request")
        self.horizontalLayout_2.addWidget(self.btn_request)
        self.btn_print = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_print.setObjectName("btn_print")
        self.horizontalLayout_2.addWidget(self.btn_print)
        self.btn_exit = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout_2.addWidget(self.btn_exit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_period_end = QtWidgets.QLabel(Form)
        self.label_period_end.setGeometry(QtCore.QRect(110, 50, 78, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_period_end.setFont(font)
        self.label_period_end.setObjectName("label_period_end")
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.label_period_start.raise_()
        self.label_period_end.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_period_start.setText(_translate("Form", "Start Period"))
        self.label_2.setText(_translate("Form", "Записей в БД"))
        self.label.setText(_translate("Form", "Последний запрос"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.btn_request.setText(_translate("Form", "Запрос"))
        self.btn_print.setText(_translate("Form", "Печать"))
        self.btn_exit.setText(_translate("Form", "Выход"))
        self.label_period_end.setText(_translate("Form", "End Period"))

