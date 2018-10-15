import requests
import json
import datetime

#Privat Bank - PB

now = datetime.datetime.now()

from_PB=(requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')).json() 


print(now.strftime("%d-%m-%Y %H:%M"))
print('\n----------------------------')
print('      Privat Bank - API')
print('----------------------------')
counter=1
for i in from_PB:
    print ('{}. {}: {:.2f} / {:.2f}'.format(counter, i['ccy'], float(i['buy']), float(i['sale'])))
    counter+=1

print('----------------------------\n')
input('To Close - press ENTER')