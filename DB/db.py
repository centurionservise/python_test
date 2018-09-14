import sqlite3

connector=sqlite3.connect('DB/test_db.db')
# connector2=sqlite3.connect('DB\testDB2.sqlite')
cursor=connector.cursor()

cursor.execute("""SELECT * FROM table1""")
result=cursor.fetchall()
print(result)

connector.close()