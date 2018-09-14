koloda = [6,7,8,9,10,2,3,4,11] * 4
zzz=22
xxx=555
yyy=999

print('koloda: ',koloda)

import random

random.shuffle(koloda)

print('koloda: ',koloda)

count = 0

print('Поиграем в очко?')

while True:
    choice = input('Будете брать карту? y/n\n')
    if choice == 'y':
        current = koloda.pop()
        print('Вам попалась карта достоинством %d'%current)
        count += current
        if count > 21:
            print('У вас %d очков.' %count)
            print('\nИзвините, но вы проиграли')
            break
        elif count == 21:
            print('\n**************************')
            print('Поздравляю, вы набрали 21!')
            print('**************************\n')
            break
        else:
            print('У вас %d очков.' %count)
    elif choice == 'n':
        print('У вас %d очков и вы закончили игру.' %count)
        break

print('До новых встреч!')