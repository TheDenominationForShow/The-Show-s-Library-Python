
import sqlite3
import os
import time
import logging
import datetime
from sys import argv
from sl_signature import SL_Signature
'''
@author:jzf
@date: 2019-11-20
@desc: 仓库模块
'''

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='Storage.log', level=logging.DEBUG, format=LOG_FORMAT)
fileHandler = logging.FileHandler(filename='Storage.log',encoding="utf-8")
logging.getLogger().addHandler(fileHandler)
DBName = "Storage.db"
def TimeStampToTime(timestamp):
	timeStruct = time.localtime(timestamp)
	return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

class SL_Storage:
    #存储类
    def __init__(self, rootdir, DBName = None):
        self.rootdir = rootdir
        if DBName is None :
            DBName = os.path.basename(os.path.abspath(rootdir))
            DBName += ".db"
            DBName = os.path.abspath(rootdir)+'\\'+ DBName
            self.DBName = DBName
            print("dname ="+DBName)
        self.conn = sqlite3.connect(DBName)
        self.cur = self.conn.cursor()
        self.cur.execute('''create table IF NOT EXISTS StorageLib(
            name varchar(256) not null,
            hash varchar(256) not null,
            size decimal(19,2) not null,
            idev varchar(256) not null,
            inode varchar(256) not null,
            path text not null,
            mtime datetime not null)
            ''')
        self.conn.commit()
        self.signature = SL_Signature(self.rootdir)

    def __del__(self):
        print('close')
        self.conn.close()
    def create_storage(self):
        '''
        创建一个.showlib文件夹
        创建一个config.xml，生成仓库的uuid等基本信息
        '''
        pass
    def open_storage(self):
        '''
        从config.xml中读取配置信息
        '''
        pass
    def delete_stroage(self):
        '''
        删除仓库
        '''
        pass
    def add_path(self):
        pass
    def del_path(self):
        pass
    def scan_path(self,root_path = None):
        '''
        扫描路径，生成db
        '''
        RootPath = os.path.abspath(self.rootdir)
        if root_path is not None:
            RootPath = os.path.abspath(self.root_path)
        logging.debug(RootPath)
        recordset = []
        for root, dirs, files in os.walk(RootPath) :
            print(root)
            for name in files :
                print(name)
                if root+'\\'+name == self.DBName:
                    continue
                self.GenRecord(root,name)
        return  recordset   
    
    def InsertToDB(self,record):
        #将记录插入到数据库
        try:
            self.conn.execute('''insert into StorageLib (name, hash, size, idev, inode, path, mtime) 
                values(?,?,?,?,?,?,?)''',tuple(record))
            self.conn.commit()
            logging.debug(record)
        except Exception as e:
            logging.debug("%s  path is %s" %(e,record[5]))

    def GenRecord(self,root,name):
        #生成单条记录并插入到库
        FileAbsPath = root+'\\'+name
        record = self.signature.GenRecord(root,name)
        record.append(str(os.stat(FileAbsPath).st_dev))
        record.append(str(os.stat(FileAbsPath).st_ino))
        record.append(FileAbsPath)
        record.append(TimeStampToTime(os.path.getmtime(FileAbsPath)))
        self.InsertToDB(record)
    def ListvedioRC(self):
        #查找视频资源
        l = []
        for row in self.conn.execute(''' SELECT * FROM StorageLib where name like  '%.avi' or name like  '%.MP4' or name like  '%.flv' or name like  '%.rmvb' or name like  '%.wmv' '''):
            l.append(row)
        self.conn.commit()
        return l
    def GetRecord_ByHash(self,hash):
        l = []
        for row in self.conn.execute(''' SELECT * FROM StorageLib where hash = ? ''',hash):
            l.append(row)
        self.conn.commit()
        return l
    def GetRecords(self):
        self.cur.execute(''' SELECT * FROM StorageLib''')
        ls = self.cur.fetchall()
        self.conn.commit()
        return ls
    def ShowRecordsCount(self):
        for row in self.conn.execute(''' SELECT count(*) FROM StorageLib'''):
            print(row)
        self.conn.commit()
    def GetHashList(self) :
        hashlist = []
        for row in self.conn.execute('SELECT distinct hash FROM StorageLib'):
            hashlist.append(row[0])
        self.conn.commit()
        return hashlist
    def ShowRepeatRC(self) :
        l = []
        l = self.GetHashList()
        sizeCount = 0 
        for h in l:
            lh = []
            lh.append(h)
            ret = self.GetRecord_ByHash(lh)
            if len(ret) > 1:
                print('hash is %s num is %d' %(h,len(ret)))
                print('=========================================')
                index = 0
                for item in ret:
                    print("FileName %s" %item[0])
                    print("    |__size %s" %item[2])
                    print("    |__Path %s" %item[4])
                    print('')
                    if index != 0 :
                        sizeCount += item[2]
                    index += 1
                print('')
        print('冗余大小约为 %d' %sizeCount)

if __name__ == "__main__" :
    # 使用xx.py xxx路径
    old = datetime.datetime.now()
    print(old.strftime('%Y-%m-%d %H:%M:%S.%f'))  
    f = SL_Storage(argv[1])
    if argv[2] == "scan":
        f.scan_path()
    elif argv[2] == "ShowRepeat":
        f.ShowRepeatRC()
    elif argv[2] == "ListvedioRC":
        l = f.ListvedioRC()
        print(l)
    elif argv[2] == "ShowRecordsCount":
        f.ShowRecordsCount()
    
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    print(datetime.datetime.now()-old)