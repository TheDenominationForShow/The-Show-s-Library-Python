import os 
import hashlib
import sqlite3

# Generate single file hash code
def GenerateFileHash( FileName ) :
    hs = hashlib.sha256()
    with open(FileName,'rb') as f:
        byte = f.read(512)
        hs.update(byte)
    return hs.hexdigest()

# 
conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS SRCLIB(
        name            varchar(256) NOT NULL,
        hash            varchar(256) NOT NULL,
        size            numeric(18,5) NOT NULL,
        mtine           datetime NOT NULL,
        path            varchar(256));
        ''')
conn.commit()
conn.close()