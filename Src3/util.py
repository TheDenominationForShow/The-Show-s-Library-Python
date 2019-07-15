
import hashlib
import time
import logging
import datetime

def TimeStampToTime(timestamp):
	timeStruct = time.localtime(timestamp)
	return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

def GetFileHash( FileName ) :
	hs = hashlib.sha256()
	with open(FileName,'rb') as f:
		byte = f.read(512)
		hs.update(byte)
	return hs.hexdigest()

if __name__ == "__main__":
    pass