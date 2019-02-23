import sqlite3
import logging
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='Manager.log', level=logging.INFO, format=LOG_FORMAT)
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
    def __del__(self):
        #self.conn.close()
        pass
    # 加载插件
    def LoadAddin(self):
        pass
    # 卸载插件
    def UnLoadAddin(self):
        pass
    
    #向资源列表添加hash值
    def AddRecordToRCHashTable(self,record):
        conn = sqlite3.connect("ShowLib.db")
        cur = conn.cursor()
        try:
            cur.execute('''insert into RCHashTable(hash,name,size,mtime) values(?,?,?,?)''',record)
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            conn.close()
        #向资源列表添加hash值
    def AddRecordsToRCHashTable(self,records):
        conn = sqlite3.connect("ShowLib.db")
        cur = conn.cursor()
        for record in records:
            try:
                cur.execute('''insert into RCHashTable(hash,name,size,mtime) values(?,?,?,?)''',record)
                conn.commit()
            except Exception as e:
                print(e)
                continue
        conn.close()

    #向资源列表添加hash值
    def AddRecordToRCHashTableNeedConn(self,record,conn):
        cur = conn.cursor()
        try:
            cur.execute('''insert into RCHashTable(hash,name,size,mtime) values(?,?,?,?)''',record)
            conn.commit()
        except Exception as e:
            logging.warn(e)
    #打印前100个记录
    def GetRecordList(self):
        conn = sqlite3.connect("ShowLib.db")
        cur = conn.cursor()
        retRecords = []
        try:
            cur.execute('''select  * from RCHashTable''')
            retRecords = list(cur.fetchall())
        except Exception as e:
            print(e)
        finally :
            conn.close()
            return retRecords
    #展示记录数
    def ShowRecordCount(self):
        conn = sqlite3.connect("ShowLib.db")
        cur = conn.cursor()
        try:
            cur.execute('''select count(*) from RCHashTable''')
            retlist = cur.fetchall()
            if len(retlist) == 1:
                return retlist[0][0]
            else :
                return 0
        except Exception as e:
            print(e)
            return 0
if __name__ == '__main__':
    pass