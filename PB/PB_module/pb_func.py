import requests
import json
import datetime
import sqlite3
import os, sys
import msvcrt


line='----------------------------------------------'
line_header='''----------------------------------------------
            Privat Bank - API
----------------------------------------------'''


def records_count(cursor):
    '''Function return amount of records in DB'''
    cursor.execute("SELECT * FROM Exchange_Rates WHERE ccy='USD'")
    row=cursor.fetchall()
    return(len(row))

def db_connect(db_name):
    '''Function get DB name, connects and return DB Tuple - (connector, cursor)'''
    try:
        connector=sqlite3.connect(db_name)
        cursor=connector.cursor()
        return (connector,cursor)
        # return True
    except:
        print("Was an error witn Data Base...")
        return (None, None)

def get_req(temp_url):
    '''Function get Url and returns result of request''' 
    try:
        return (requests.get(temp_url)).json()
    except requests.status_codes as status:
        print("Was an error witn request...")
        print("Status: ", status)
        return None

def main_func(from_PB, cursor, connector,privat_txt):
    temp_id=records_count(cursor)+1
    temp_list=[]
    temp_time=None
    now = datetime.datetime.now()

    if from_PB!=None:
            temp_time=now.strftime("%d-%m-%Y %H:%M:%S")
            print(temp_time)
            print(line_header)
            counter=1
            for i in from_PB:
                line_main='{}. {}: buy - {:.2f} {} / sale - {:.2f} {}'.format(counter, i['ccy'], float(i['buy']), i['base_ccy'], float(i['sale']),i['base_ccy'])
                temp_list.append(line_main)
                print(line_main)
                counter+=1
                try:
                    cursor.execute("INSERT INTO Exchange_Rates (id,ccy,base_ccy,buy,sale,date,time) VALUES (?,?,?,?,?,?,?)",(temp_id,i['ccy'], i['base_ccy'],i['buy'],i['sale'],now.strftime("%d-%m-%Y"),now.strftime("%H:%M:%S")))
                except sqlite3.DatabaseError as err:
                    print("Error SQLite3: ", err)
                else:
                    connector.commit()
            print(line)
    else:
        print("Chack Internet Connection or PrivatBank API")


    with open(privat_txt,'w') as file:
        file.write(temp_time)
        file.write('\n'+line_header)
        for elem in temp_list:
            file.write('\n'+elem)
        file.write('\n'+line)

