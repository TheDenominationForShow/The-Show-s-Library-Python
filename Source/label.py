import sqlite3
import logging
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
         
    def addLabel(self,record):
        record.append(0)
        record.append(0)
        try:
            self.cur.execute('''insert into RCLabelTable(lable,hash,desc,pro,con) values(?,?,?,?,?)''',record)
            self.conn.commit()
        except Exception as e:
            logging.warn(e)

    def proLabel(self,hash,label):
        records = self.getRecordByPrimaryKey(hash,label)
        if len(records) is 0:
            pass
        try:
            self.cur.execute(''' update RCLabelTable set  pro = pro+1 where hash = ? label = ?''',(hash,label))
            self.conn.commit()
        except Exception as e:
            logging.warn(e)

    def conLabel(self,hash,label):
        records = self.getRecordByPrimaryKey(hash,label)
        if len(records) is 0:
            return 
        if records[0][4] < 1 is True:
            return
        try:
            self.cur.execute(''' update RCLabelTable set  con = con-1 where hash = ? label = ?''',(hash,label))
            self.conn.commit()
        except Exception as e:
            logging.warn(e)
    
    #根据hash获取标签集合
    def getlabelsByHash(self,hashstr):
        try:
            c = self.cur.execute('''select * from RCLabelTable where hash = ?''',hasattr)
            recordsets = c.fetchall()
        except Exception as e:
            logging.warn(e)
        else:
            return recordsets

    #根据标签获取hash集合
    def getHashsByLabel(self,labelstr):
        try:
            c = self.cur.execute('''select * from RCLabelTable where label = ?''',labelstr)
            recordsets = c.fetchall()
        except Exception as e:
            logging.warn(e)
        else:
            return recordsets

    #根据 hash和标签 返回一个值
    def getRecordByPrimaryKey(self,hashstr,labelstr):
        try:
            c = self.cur.execute('''select * from RCLabelTable where label = ? and hash = ?''',(labelstr,hashstr))
            recordsets = c.fetchall()
        except Exception as e:
            logging.warn(e)
        else:
            return recordsets

    