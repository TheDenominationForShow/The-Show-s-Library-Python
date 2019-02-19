import hashlib
import sqlite3
import os
import time
import logging
import datetime
import threading
import time
# init log config
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='my.log', level=logging.INFO, format=LOG_FORMAT)

def TimeStampToTime(timestamp):
	timeStruct = time.localtime(timestamp)
	return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

sqdb = 'test.db'

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self,rootpath):
        threading.Thread.__init__(self)
        self.rootpath = rootpath
    def run(self):
        print ("开始线程：")
        GenerateDB(self.rootpath,sqdb)
        print ("退出线程：")

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# just use only the top 2048 byte
def FastGetFileHash( FileName ) :
	hs = hashlib.sha256()
	with open(FileName,'rb') as f:
		byte = f.read(2048)
		hs.update(byte)
	return hs.hexdigest()
def GenRecord(root,name):
    record = []
    record.append(name)
    FileAbsPath = root+'\\'+name
    h = FastGetFileHash(FileAbsPath)
    record.append(h)
    record.append(os.path.getsize(FileAbsPath))
    record.append(TimeStampToTime(os.path.getmtime(FileAbsPath)))
    record.append(FileAbsPath)
    logging.debug(record)
    return record
def TraversePathAndGenRecord(rootpath):
	RootPath = os.path.abspath(rootpath)
	logging.debug(RootPath)
	recordset = []
	for root, dirs, files in os.walk(RootPath) :
		for name in files :
			record = GenRecord(root,name)
			recordset.append(tuple(record))
	return  recordset

def GenerateDB(RootPath,DBName = None):
	if DBName is None:
		logging.info(RootPath)
		logging.info(os.path.abspath(RootPath))
		DBName = os.path.basename(os.path.abspath(RootPath))
		DBName += ".db"
		logging.info(DBName)
	conn = sqlite3.connect(DBName)
	c = conn.cursor()
	c.execute('''create table IF NOT EXISTS srclib(
	name varchar(256) not null,
	hash varchar(256) not null,
	size decimal(19,2) not null,
	mtime datetime not null,
	path text not null)
	''')
	conn.commit()
	li = TraversePathAndGenRecord(RootPath)
	c.executemany('''insert into srclib (name, hash, size, mtime, path) 
	values(?,?,?,?,?)''',li)
	conn.commit()
	conn.close()
	logging.info("GenerateDB SECCUSS")

def test():
    old = datetime.datetime.now()
    print(old.strftime('%Y-%m-%d %H:%M:%S.%f'))
    threadLists = []
    l = os.listdir('F:\\KS安装包\\')
    print(l)
    for item in l:
        if os.path.isdir('F:\\KS安装包\\'+item) is True:      
            thread = myThread('F:\\KS安装包\\'+item)
            threadLists.append(thread)
        else :
            continue
    # 开启新线程
    for i in threadLists:
        i.start()
    for i in threadLists:
        i.join()
    print ("退出主线程")
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    print(datetime.datetime.now()-old)
if __name__ == "__main__" :
	test()