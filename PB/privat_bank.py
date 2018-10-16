import requests
import json
import datetime
import sqlite3
import os

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

line1='----------------------------------------------'
line2='            Privat Bank - API'
# line1='\n----------------------------------------------'

if from_PB!=None:


    with open('PB/privat_api.txt','w') as file:
        # file.write( )
        # file.close()

        print(now.strftime("%d-%m-%Y %H:%M:%S"))

        file.write(now.strftime("%d-%m-%Y %H:%M:%S"))
        file.write('\n'+line1)
        file.write('\n'+line2)
        file.write('\n'+line1)
        # print('\n----------------------------------------------')
        print(line1)
        print(line2)
        print(line1)
        # print('      Privat Bank - API')
        # print('----------------------------------------------')
        counter=1
        for i in from_PB:
            line_main='{}. {}: buy - {:.2f} {} / sale - {:.2f} {}'.format(counter, i['ccy'], float(i['buy']), i['base_ccy'], float(i['sale']),i['base_ccy'])
            # print ('{}. {}: buy - {:.2f} {} / sale - {:.2f} {}'.format(counter, i['ccy'], float(i['buy']), i['base_ccy'], float(i['sale']),i['base_ccy']))
            file.write('\n'+line_main)
            print(line_main)
            counter+=1
            cursor.execute("INSERT INTO Exchange_Rates (ccy,base_ccy,buy,sale,date,time) VALUES (?,?,?,?,?,?)",(i['ccy'], i['base_ccy'],i['buy'],i['sale'],now.strftime("%d-%m-%Y"),now.strftime("%H:%M:%S")))
            connector.commit()


        # print('\n----------------------------------------------')
        print(line1)
        file.write('\n'+line1)
        file.close()
    # print(from_PB)
    # input('To Close - press ENTER')
else:
    print("Chack Internet Connection or PrivatBank API")

print("- Show all records [enter 1]")
print("- Exit  [enter 2]")
print("- Print  [enter 3]")

answer=input()

if answer=="1":
    show_all_records()
elif answer=="2":
    print("Buy")
elif answer=="3":
    os.startfile('privat_api.txt', "print")

with open( 'privat_api.txt' , 'r' ) as file:
    ccc=file.readlines()
    file.close()

print("From privat_api.txt:\n",ccc)

# os.startfile('privat_api.txt', "print")