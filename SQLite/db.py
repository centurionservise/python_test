import sqlite3
import random
import string
from os import mkdir


# DB='DB/test_db.db'
DB='SQLite/test_db.db'


# 1
try:
    connector=sqlite3.connect(DB)
    cursor=connector.cursor()
except sqlite3.OperationalError:
    print('Try #1')
    mkdir('DB')
# finally:
#     connector=sqlite3.connect(DB)
#     cursor=connector.cursor()

# 2
try:
    cursor.execute("""CREATE TABLE sclad (id int auto_increment primary key,name varchar, cost varchar, amount varchar)""")
except:
    print('Try #2')


def ins_rand_rec():

    list_temp=[]

    for i in string.ascii_letters:
        list_temp.append(i)


    rand_age=random.randint(20,80)

    rand_phone="+380" + str(random.randint(500000000,800000000))

    random.shuffle(list_temp)

    rand_name=''.join(c for c in list_temp)
    rand_name=rand_name[:8]


    # 3
    try:
        cursor.execute("insert into table2 (ownerName,ownerAge,ownerPhoneNumber) values ('{0}', {1}, {2})".format(rand_name, rand_age,rand_phone))
        # connector.commit()
    except:
        cursor.execute("""CREATE TABLE table2 (id integer primary key,ownerName varchar, ownerAge varchar, ownerPhoneNumber varchar)""")
        print('Try #3')
    # finally:
    #     cursor.execute("insert into table2 (ownerName,ownerAge,ownerPhoneNumber) values ('{0}',{1},{2})".format(rand_name, rand_age,rand_phone))
    #     connector.commit()

for i in range(10000):
    ins_rand_rec()

connector.commit()




#7 Вывод всех записей таблицы

cursor.execute("select * from table2")
row=cursor.fetchone()

while row:
    print(row[0], row[1], row[2], row[3])
    row=cursor.fetchone()
# 7



cursor.close()
connector.close()

# +380 677 307 424