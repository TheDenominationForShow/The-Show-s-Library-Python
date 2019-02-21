import sqlite3

class UserManager:
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
        pass
    def __del__(self):
        pass
    def addUser(self):
        pass
    def delUser(self):
        pass
    def SearchUser(self):
        pass
    def ModifyUser(self):
        pass