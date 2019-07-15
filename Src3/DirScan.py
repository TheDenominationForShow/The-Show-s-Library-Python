import hashlib
import sqlite3
import os
import time
import logging
import datetime
from sys import argv
import uuid
# init log config
#log = logging.getLogger()
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='finder.log', level=logging.DEBUG, format=LOG_FORMAT)

def TimeStampToTime(timestamp):
	timeStruct = time.localtime(timestamp)
	return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

def GetFileHash( FileName ) :
	hs = hashlib.sha256()
	with open(FileName,'rb') as f:
		byte = f.read(512)
		hs.update(byte)
	return hs.hexdigest()

class DirScanner:
    def __init__(self, workDir):
        self.workDir = workDir
        DBName = "scanner.db"
        DBName = self.workDir + os.sep + DBName
        self.conn = sqlite3.connect(DBName)
        self.cur = self.conn.cursor()
        self.cur.execute('''create table IF NOT EXISTS scanner(
            name varchar(256) not null,
            st_ino varchar(256) not null,
            st_dev varchar(256) not null,
            st_size decimal(19,2) not null,
            atime datetime not null,
            mtime datetime not null,
            scantime datetime not null)
            ''')
        self.conn.commit()
    def __del__(self):
        print('scanner close')
        self.conn.close()

    def scan_dir(self,dest_dir):
        pass

if __name__ == "__main__" :
	pass

