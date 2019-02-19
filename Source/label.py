import sqlite3

def CreateDB():
    conn = sqlite3.connect("ShowLib.db")
    c = conn.cursor()
    c.execute('''create table IF NOT EXISTS RCLabelTable(
    lable varchar(256) not null ,
    hash varchar(256) not null,
    size decimal(19,2) not null,
    mtime datetime not null)
    ''')
    conn.commit()
    conn.close()