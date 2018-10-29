import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
from PyQt5 import uic
from PyQt5 import QtWidgets
from Ui_pb_gui import Ui_Form

import requests
import json
import datetime
import sqlite3
import os, sys
import msvcrt
# from PB_module import pb_func

# DB='privat_api.db'
# privat_txt='privat_api.txt'
# url='https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

# cursor=None
# connector=None

# import design  # Это наш конвертированный файл дизайна

class SergWindow(QtWidgets.QMainWindow, Ui_Form):
    cursor=None
    connector=None

    def __init__(self):
        self.DB='privat_api.db'
        self.privat_txt='privat_api.txt'
        self.url='https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
        # cursor=None
        # connector=None
        self.line='----------------------------------------------'
        self.line_header='''----------------------------------------------
            Privat Bank - API
            ----------------------------------------------'''
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        # self.setWindowTitle("Hello world")
        self.connector, self.cursor=self.db_connect()
        self.lcdNumber.display(self.records_count())
        # self.btn_request.clicked.connect(self.main_func(self.get_req(self.url),self.cursor, self.connector,self.privat_txt))
        self.btn_request.clicked.connect(self.main_func)
    
    # def CopyText(self):
    #     self.textEdit_1.append(self.lineEdit_1.text())
    #     self.lineEdit_1.setText("SERG")
    #     # window.setWindowTitle("PyQt")
    #     pass

    def records_count(self):
        '''Function return amount of records in DB'''
        try:
            self.cursor.execute("SELECT * FROM Exchange_Rates WHERE ccy='USD'")
            row=self.cursor.fetchall()
            return(len(row))
        except sqlite3.DatabaseError as DB_error:
            # print("def records_count ->")
            # print("Error was found with DB or table ...")
            print("sqlite3.DatabaseError: ",DB_error)
            return 0

    def db_connect(self):
        '''Function get DB name, connects and return DB Tuple - (connector, cursor)'''
        try:
            connector=sqlite3.connect(self.DB)
            cursor=connector.cursor()
            new_table="CREATE TABLE IF NOT EXISTS Exchange_Rates (id INTEGER,ccy STRING,base_ccy STRING,buy REAL,sale REAL,date TEXT,time TEXT)"
            cursor.execute(new_table)
            return (connector,cursor)
        except sqlite3.DatabaseError as DB_error:
            print("sqlite3.DatabaseError: ", DB_error)
            return (None, None)

    def get_req(self, temp_url):
        '''Function gets Data by Url and returns result of request''' 
        try:
            # print("ZZZ")
            return (requests.get(temp_url)).json()
        except :
            print("There was an error with the request")
            print("Cheack Internet Connection or PrivatBank API url")
            return None

    def main_func(self):
        from_PB=self.get_req(self.url)
        temp_id=self.records_count()+1
        # print(temp_id)
        temp_list=[]
        temp_time=None
        now = datetime.datetime.now()
        self.textEdit.clear()
        # print(now)

        if from_PB!=None:
            temp_time=now.strftime("%d-%m-%Y %H:%M:%S")
            self.label_date.setText(temp_time)
            # print(temp_time)
            # print(self.line_header)
            counter=1
            for i in from_PB:
                line_main='{}. {}: buy - {:.2f} {} / sale - {:.2f} {}'.format(counter, i['ccy'], float(i['buy']), i['base_ccy'], float(i['sale']),i['base_ccy'])
                temp_list.append(line_main)
                # print(line_main)
                self.textEdit.append(line_main)
                counter+=1
                # print(counter)
                try:
                    self.cursor.execute("INSERT INTO Exchange_Rates (id,ccy,base_ccy,buy,sale,date,time) VALUES (?,?,?,?,?,?,?)",(temp_id,i['ccy'], i['base_ccy'],i['buy'],i['sale'],now.strftime("%d-%m-%Y"),now.strftime("%H:%M:%S")))
                    # pass
                    # print("record added")
                except sqlite3.DatabaseError as err:
                    print("Error SQLite3: ", err)
                else:
                    self.connector.commit()
            # print(self.line)

            with open(self.privat_txt,'w') as file:
                file.write(temp_time)
                file.write('\n'+self.line_header)
                for elem in temp_list:
                    file.write('\n'+elem)
                file.write('\n'+self.line)

            self.lcdNumber.display(self.records_count())
        
        else:
            # print("Chack Internet Connection or PrivatBank API url")
            pass
        # print("Exit Function")


    # def browse_folder(self):
    #     self.listWidget.clear()  # На случай, если в списке уже есть элементы
    #     directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")

    #     if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
    #         for file_name in os.listdir(directory):  # для каждого файла в директории
    #             self.listWidget.addItem(file_name)   # добавить файл в listWidget

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = SergWindow()  # Создаём объект класса SergWindow
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
    # print("Buy-buy")

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()