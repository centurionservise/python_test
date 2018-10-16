import sqlite3
import random
import string


DB='DB/test_db.db'

# D:\Users\Администратор\Desktop\Python\CODE\DB\test_db1.db
# DB\test_db.db

# last_id=1


try:
    connector=sqlite3.connect(DB)
    cursor=connector.cursor()
except:
    pass

# try:
#     cursor.execute("""SELECT * FROM table2""")
#     result=cursor.fetchall()
#     print(result)
# except:
#     print("Empty %s !" % (DB))

cursor.execute("select * from table2")
row=cursor.fetchone()

while row:
    print(row)
    print(row[0], row[1], row[2], row[3])
    # print(row[1]+'\n')
    last_id=row[0]
    row=cursor.fetchone()


# list_letters=string.ascii_letters
# list_digits=string.digits

# print(list_letters)
# print(list_digits)

list_temp=[]

for i in string.ascii_letters:
   list_temp.append(i)

    # z=random.randint(32,128)
    # list_temp.append(chr(z))


rand_age=random.randint(20,80)
rand_phone=random.randint(1000000,5000000)

# print(list_temp)
random.shuffle(list_temp)
# print(list_temp)

rand_name=''.join(c for i,c in enumerate(list_temp) if i<10 )
# print(list_temp)
# print(string.ascii_lowercase)
# print(rand_name)


# cursor.execute("INSERT INTO table2 (ownerAge,ownerPhoneNumber,Name) VALUES (%s,%s,%s)"%(rand_age,rand_phone,rand_name))
# cursor.execute("INSERT INTO table2 (ownerAge,ownerPhoneNumber) VALUES (%s,%s)"%(rand_age,rand_phone))
cursor.execute("INSERT INTO table2 (Name,ownerPhoneNumber,ownerAge) VALUES (?,?,?)",(rand_name,rand_phone,rand_age))

connector.commit()




cursor.close()
connector.close()