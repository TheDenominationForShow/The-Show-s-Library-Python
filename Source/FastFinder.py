import hashlib
import sqlite3
import os
import time
import logging

# init log config
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)

def TimeStampToTime(timestamp):
	timeStruct = time.localtime(timestamp)
	return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

# just use only the top 2048 byte
def FastGetFileHash( FileName ) :
	hs = hashlib.sha256()
	with open(FileName,'rb') as f:
		byte = f.read(2048)
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
			h = FastGetFileHash(FileAbsPath)
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

if __name__ == "__main__" :
	GenerateDB('H:\MY_INTEREST\Move\h')