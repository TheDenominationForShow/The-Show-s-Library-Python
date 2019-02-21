import sqlite3

class ShowLibManager:
    def __init__(self):
        pass
    def __del__(self):
        pass
    # 加载插件
    def LoadAddin(self):
        pass
    def UnLoadAddin(self):
        pass
    
    
def CreateDB():
    conn = sqlite3.connect("ShowLib.db")
    c = conn.cursor()
    c.execute('''create table IF NOT EXISTS RCHashTable(
    hash varchar(256) not null primary key,
    name varchar(256) not null,
    size decimal(19,2) not null,
    mtime datetime not null)
    ''')
    conn.commit()
    conn.close()

def AddRecordToRCHashTable(record):
    conn = sqlite3.connect("ShowLib.db")
    c = conn.cursor()
    try:
        c.execute('''insert into RCHashTable(hash,name,size,mtime) values(?,?,?,?)''',record)
    except Exception as e:
        print(e)
    else:
        conn.commit()

def ShowRecordCount():
    conn = sqlite3.connect("ShowLib.db")
    c = conn.cursor()
    for row in c.execute('''select count(*) from RCHashTable'''):
        print(row)

def ShowRecordList():
    conn = sqlite3.connect("ShowLib.db")
    c = conn.cursor()
    for row in c.execute('''select  * from RCHashTable limit 100'''):
        print(row)

if __name__ == '__main__':
    ShowRecordCount()
    ShowRecordList()