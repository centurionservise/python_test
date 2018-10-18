import requests
import json
import datetime
import sqlite3
import os, sys
import msvcrt

#Privat Bank - PB
DB='PB/privat_api.db'
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


with open( 'privat_api.txt' , 'r' ) as file:
        file_content=file.readlines()
print("From privat_api.txt:\n",file_content)


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

with open('PB/privat_api.txt','w') as file:
    file.write(temp_time)
    file.write('\n'+line_header)
    for elem in temp_list:
        file.write('\n'+elem)
    file.write('\n'+line)
    # file.close()

# print(temp_list)




print("- Show all records pr. 1")
print("- Exit  pr. 2")
print("- Print  pr. 3")
print("- Read File pr. 4")

key = msvcrt.getch()
file_content=None

if str(key)=="b'1'":
    show_all_records()
elif str(key)=="b'2'":
    print("Buy")
elif str(key)=="b'3'":
    os.startfile('privat_api.txt', "print")
elif str(key)=="b'4'":
    with open( 'privat_api.txt' , 'r' ) as file:
        file_content=file.readlines()
        # file_content=file.read()
        # for line_in_file in file:
        #     print(line_in_file)
        # file.close()

# print("From privat_api.txt:\n",file_content)

# os.startfile('privat_api.txt', "print")