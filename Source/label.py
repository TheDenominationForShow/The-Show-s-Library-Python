import sqlite3

class Labeler:
    def __init__(self):
        self.conn = sqlite3.connect("ShowLib.db")
        self.cur = self.conn.cursor()
        self.cur.execute('''create table IF NOT EXISTS RCLabelTable(
            lable varchar(256) not null,
            hash varchar(256) not null,
            desc text,
            pro int default 0,
            con int default 0,
            primary key(lable,hash))
        ''')
        self.conn.commit()
    def __del__(self):
         self.conn.close()
         
    def addLabel(self):
        pass
    def proLabel(self):
        pass
    def conLabel(self):
        pass
    def getlabelByHash(self,hashstr):
        pass
    