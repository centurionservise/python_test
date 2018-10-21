import requests
import json
import datetime
import sqlite3
import os, sys
import msvcrt

#Privat Bank - PB
DB='privat_api.db'
try:
    connector=sqlite3.connect(DB)
    cursor=connector.cursor()
except:
    print("Was an error witn Data Base...")

def show_all_records():

    cursor.execute("select * from Exchange_Rates")
    row=cursor.fetchone()

    while row:
        print(row)
        row=cursor.fetchone()

now = datetime.datetime.now()
from_PB=None

try:
    from_PB=(requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')).json()
except:
    print("Was an error witn request...")

line='----------------------------------------------'
line_header='''----------------------------------------------
            Privat Bank - API'
----------------------------------------------'''
temp_list=[]
temp_time=None
if from_PB!=None:
        temp_time=now.strftime("%d-%m-%Y %H:%M:%S")
        print(temp_time)
        print(line_header)
        counter=1
        for i in from_PB:
            line_main='{}. {}: buy - {:.2f} {} / sale - {:.2f} {}'.format(counter, i['ccy'], float(i['buy']), i['base_ccy'], float(i['sale']),i['base_ccy'])
            # print ('{}. {}: buy - {:.2f} {} / sale - {:.2f} {}'.format(counter, i['ccy'], float(i['buy']), i['base_ccy'], float(i['sale']),i['base_ccy']))
            temp_list.append(line_main)
            print(line_main)
            counter+=1
            cursor.execute("INSERT INTO Exchange_Rates (ccy,base_ccy,buy,sale,date,time) VALUES (?,?,?,?,?,?)",(i['ccy'], i['base_ccy'],i['buy'],i['sale'],now.strftime("%d-%m-%Y"),now.strftime("%H:%M:%S")))
            connector.commit()
        print(line)
else:
    print("Chack Internet Connection or PrivatBank API")

with open('privat_api.txt','w') as file:
    file.write(temp_time)
    file.write('\n'+line_header)
    for elem in temp_list:
        file.write('\n'+elem)
    file.write('\n'+line)


# print("Show BD records - s")
# print("Print - p")
# print("Exit - q")

# key = msvcrt.getch()
# file_content=None

while True:
    print('********************')
    print("Show BD records - s")
    print("Print - p")
    print("Exit - q")
    print('********************')

    key = msvcrt.getch()
    file_content=None

    if str(key)=="b's'":
        show_all_records()
        # break
    elif str(key)=="b'q'":
        print("Buy")
        break
    elif str(key)=="b'p'":
        os.startfile('privat_api.txt', "print")
    # elif str(key)=="b'4'":
    #     with open( 'privat_api.txt' , 'r' ) as file:
    #         file_content=file.readlines()
    #     print("From privat_api.txt:\n",file_content)