import requests
import json
import datetime
import sqlite3
import os, sys
import msvcrt
from PB_module import pb_func

DB='privat_api.db'
privat_txt='privat_api.txt'
url='https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

cursor=None
connector=None


connector,cursor=pb_func.db_connect(DB)


pb_func.main_func(pb_func.get_req(url),cursor, connector,privat_txt)

while True:
    print('********************')
    print("Print - p")
    print("Exit - q")
    print("Records Count - c")
    print("New request - n")
    print('********************')

    key = msvcrt.getch()
    file_content=None

    if str(key)=="b'n'":
        pb_func.main_func(pb_func.get_req(url), cursor, connector, privat_txt)
    elif str(key)=="b'q'":
        print("Buy")
        break
    elif str(key)=="b'p'":
        os.startfile('privat_api.txt', "print")
    elif str(key)=="b'c'":
        print('Records count = ',pb_func.records_count(cursor))

