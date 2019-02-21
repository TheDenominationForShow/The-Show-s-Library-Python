import sqlite3

class Manager:
    def __init__(self):
        self.conn = sqlite3.connect("ShowLib.db")
        self.cur = self.conn.cursor()
        self.cur.execute('''create table IF NOT EXISTS RCHashTable(
        hash varchar(256) not null primary key,
        name varchar(256) not null,
        size decimal(19,2) not null,
        mtime datetime not null)
        ''')
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    #向资源列表添加hash值
    def AddRecordToRCHashTable(self,record):
        try:
            self.cur.execute('''insert into RCHashTable(hash,name,size,mtime) values(?,?,?,?)''',record)
            self.conn.commit()
        except Exception as e:
            print(e)
    
    #打印前100个记录
    def ShowRecordList(self):
        for row in self.cur.execute('''select  * from RCHashTable limit 100'''):
            print(row)
    #展示记录数
    def ShowRecordCount(self):
        for row in self.cur.execute('''select count(*) from RCHashTable'''):
            print(row)
            
if __name__ == '__main__':
    pass