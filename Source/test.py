import sqlite3
DBName = 'h.db'
conn = sqlite3.connect(DBName)
c = conn.cursor()

des = c.execute('select count(*) FROM srclib')
des = c.fetchall()
print(des)