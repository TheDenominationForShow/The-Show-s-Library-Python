import sqlite3

class ShowLibManager:
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
        self.conn.close()
    #
    def __del__(self):
        pass
    # 加载插件
    def LoadAddin(self):
        pass
    # 卸载插件
    def UnLoadAddin(self):
        pass

    def AddRecordToRCHashTable(self,record):
        #self.conn = sqlite3.connect("ShowLib.db")
        #self.cur = self.conn.cursor()
        try:
            self.cur.execute('''insert into RCHashTable(hash,name,size,mtime) values(?,?,?,?)''',record)
        except Exception as e:
            print(e)
        else:
            self.conn.commit()

    def ShowRecordCount(self):
        for row in self.cur.execute('''select count(*) from RCHashTable'''):
            print(row)

    def ShowRecordList(self):
        #conn = sqlite3.connect("ShowLib.db")
        #c = conn.cursor()
        for row in self.cur.execute('''select  * from RCHashTable limit 100'''):
            print(row)

if __name__ == '__main__':
    ShowRecordCount()
    ShowRecordList()