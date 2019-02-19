import hashlib
import sqlite3
import os
import time
import logging
import datetime
# init log config
#log = logging.getLogger()
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)

def TimeStampToTime(timestamp):
	timeStruct = time.localtime(timestamp)
	return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

def GetFileHash( FileName ) :
	hs = hashlib.sha256()
	with open(FileName,'rb') as f:
		byte = f.read(512)
		hs.update(byte)
	return hs.hexdigest()

def TraversePathAndGenRecord(rootpath):
	RootPath = os.path.abspath(rootpath)
	logging.debug(RootPath)
	recordset = []
	for root, dirs, files in os.walk(RootPath) :
		for name in files :
			record = []
			record.append(name)
			FileAbsPath = root+'\\'+name
			h = GetFileHash(FileAbsPath)
			record.append(h)
			record.append(os.path.getsize(FileAbsPath))
			record.append(TimeStampToTime(os.path.getmtime(FileAbsPath)))
			record.append(FileAbsPath)
			logging.debug(record)
			recordset.append(tuple(record))
	return  recordset

def GenerateDB(RootPath,DBName = None):
	if DBName is None:
		DBName = os.path.basename(os.path.abspath(RootPath))
		DBName += ".db"
		DBName = os.path.abspath(RootPath)+ DBName
	conn = sqlite3.connect(DBName)
	c = conn.cursor()
	c.execute('''create table IF NOT EXISTS srclib(
	name varchar(256) not null,
	hash varchar(256) not null,
	size decimal(19,2) not null,
	mtime datetime not null,
	path text not null primary key)
	''')
	conn.commit()
	li = TraversePathAndGenRecord(RootPath)
	c.executemany('''insert into srclib (name, hash, size, mtime, path) 
	values(?,?,?,?,?)''',li)
	conn.commit()
	conn.close()

class Finder:
    def __init__(self, rootdir, DBName = None):
        self.rootdir = rootdir
        if DBName is None:
            DBName = os.path.basename(os.path.abspath(rootdir))
            DBName += ".db"
            DBName = os.path.abspath(rootdir)+'\\'+ DBName
            print(DBName)
        self.conn = sqlite3.connect(DBName)
        self.cur = self.conn.cursor()
        self.cur.execute('''create table IF NOT EXISTS srclib(
            name varchar(256) not null,
            hash varchar(256) not null,
            size decimal(19,2) not null,
            mtime datetime not null,
            path text not null primary key)
            ''')
        self.conn.commit()

    def __del__(self):
        print('close')
        self.conn.close()

    def initDB(self):
        pass

    def GenRecord(self,root,name):
        record = []
        record.append(name)
        FileAbsPath = root+'\\'+name
        h = GetFileHash(FileAbsPath)
        record.append(h)
        record.append(os.path.getsize(FileAbsPath))
        record.append(TimeStampToTime(os.path.getmtime(FileAbsPath)))
        record.append(FileAbsPath)
        self.InsertToDB(record)

    def InsertToDB(self,record):
        try:
            self.conn.execute('''insert into srclib (name, hash, size, mtime, path) 
	            values(?,?,?,?,?)''',tuple(record))
            self.conn.commit()
            logging.debug(record)
        except Exception as e:
            logging.debug("%s  path is %s" %(e,record[4]))

    def TraversePathAndGenRecord(self):
        RootPath = os.path.abspath(self.rootdir)
        logging.debug(RootPath)
        recordset = []
        for root, dirs, files in os.walk(RootPath) :
            print(root)
            for name in files :
                print(name)
                self.GenRecord(root,name)
        return  recordset    
    def GenerateDB(self):
        self.TraversePathAndGenRecord()

if __name__ == "__main__" :
	
    old = datetime.datetime.now()
    print(old.strftime('%Y-%m-%d %H:%M:%S.%f'))
    f = Finder('..\\')
    f.GenerateDB()
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    print(datetime.datetime.now()-old)

