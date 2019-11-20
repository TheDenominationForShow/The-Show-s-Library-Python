import hashlib
import sqlite3
import os
import time
import logging
import datetime
from sys import argv

'''
@author:jzf
@date: 2019-11-20
@desc: 签名模块
'''

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='Signature.log', level=logging.DEBUG, format=LOG_FORMAT)
DBName = "Signature.db"
def TimeStampToTime(timestamp):
	timeStruct = time.localtime(timestamp)
	return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

class SL_Signature:
    #签名类
    def __init__(self, rootdir, DBName = None):
        self.rootdir = rootdir
        if DBName is None:
            DBName = os.path.basename(os.path.abspath(rootdir))
            DBName += ".db"
            DBName = os.path.abspath(rootdir)+'\\'+ DBName
            print(DBName)
        self.conn = sqlite3.connect(DBName)
        self.cur = self.conn.cursor()
        self.cur.execute('''create table IF NOT EXISTS SignatureLib(
            name varchar(256) not null,
            hash varchar(256) not null,
            size decimal(19,2) not null)
            ''')
        self.conn.commit()

    def __del__(self):
        print('close')
        self.conn.close()

    def GetFileHash(self, FileName):
        #获取FileName的hash值
        hs = hashlib.sha256()
        with open(FileName,'rb') as f:
            byte = f.read(512)
            hs.update(byte)
        return hs.hexdigest()

    def InsertToDB(self,record):
        #将记录插入到数据库
        try:
            self.conn.execute('''insert into SignatureLib (name, hash, size) 
                values(?,?,?)''',tuple(record))
            self.conn.commit()
            logging.debug(record)
        except Exception as e:
            logging.debug("%s  name is %s" %(e,record[0]))

    def GenRecord(self,root,name):
        #生成单条记录并插入到库
        record = []
        record.append(name)
        FileAbsPath = root+'\\'+name
        h = self.GetFileHash(FileAbsPath)
        record.append(h)
        record.append(os.path.getsize(FileAbsPath))
        self.InsertToDB(record)
        return record
    
    def TraversePathAndGenRecord(self,root_path = None):
        #编译路径，存库
        RootPath = os.path.abspath(self.rootdir)
        if root_path is not None:
            RootPath = os.path.abspath(self.root_path)
        logging.debug(RootPath)
        recordset = []
        for root, dirs, files in os.walk(RootPath) :
            print(root)
            for name in files :
                print(name)
                self.GenRecord(root,name)
        return  recordset   

if __name__ == "__main__" :
    # 使用xx.py xxx路径
    old = datetime.datetime.now()
    print(old.strftime('%Y-%m-%d %H:%M:%S.%f'))

    f = SL_Signature(argv[1])
    f.TraversePathAndGenRecord()

    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    print(datetime.datetime.now()-old)