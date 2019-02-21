import sqlite3
DBName = 'Visual Studio 2017.db'
conn = sqlite3.connect(DBName)
c = conn.cursor()

des = c.execute('select * FROM srclib where hash = "heh"')
rc = des.fetchall()
print(len(rc))