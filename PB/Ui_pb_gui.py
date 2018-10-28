# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Users\Администратор\Desktop\Python\CODE\PB\pb_gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(535, 440)
        self.label_date = QtWidgets.QLabel(Form)
        self.label_date.setGeometry(QtCore.QRect(20, 10, 78, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 40, 152, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(26, 81, 481, 254))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_request = QtWidgets.QPushButton(self.widget1)
        self.btn_request.setObjectName("btn_request")
        self.horizontalLayout_2.addWidget(self.btn_request)
        self.btn_print = QtWidgets.QPushButton(self.widget1)
        self.btn_print.setObjectName("btn_print")
        self.horizontalLayout_2.addWidget(self.btn_print)
        self.btn_exit = QtWidgets.QPushButton(self.widget1)
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout_2.addWidget(self.btn_exit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textEdit.raise_()
        self.label.raise_()
        self.btn_request.raise_()
        self.btn_print.raise_()
        self.btn_exit.raise_()
        self.label_2.raise_()
        self.lcdNumber.raise_()
        self.label_2.raise_()
        self.label_date.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_date.setText(_translate("Form", "Время / Дата"))
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

