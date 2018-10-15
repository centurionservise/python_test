import requests
import json
import datetime

#Privat Bank - PB

now = datetime.datetime.now()
from_PB=None

try:
    from_PB=(requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')).json()
except:
    print("Was an error witn request...")

if from_PB!=None:
    print(now.strftime("%d-%m-%Y %H:%M"))
    print('\n----------------------------')
    print('      Privat Bank - API')
    print('----------------------------')
    counter=1
    for i in from_PB:
        print ('{}. {}: buy-{:.2f} / sale-{:.2f}'.format(counter, i['ccy'], float(i['buy']), float(i['sale'])))
        counter+=1

    print('----------------------------\n')
    # print(from_PB)
    input('To Close - press ENTER')
else:
    print("Chack Internet Connection or PrivatBank API")