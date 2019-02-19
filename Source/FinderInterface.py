import sqlite3
DBName = '../The-Show-s-Library-Python.db'
conn = sqlite3.connect(DBName)
c = conn.cursor()

def GetHashList() :
    hashlist = []
    for row in conn.execute('SELECT distinct hash FROM srclib'):
        hashlist.append(row[0])
    return hashlist

def GetFileByHash(h) :
    l = []
    for row in conn.execute(''' SELECT * FROM srclib where hash = ? ''',h):
        l.append(row)
    return l

def ListvedioRC():
    l = []
    for row in conn.execute(''' SELECT * FROM srclib where name like  '%.avi' or name like  '%.MP4' or name like  '%.flv' or name like  '%.rmvb' or name like  '%.wmv' '''):
        l.append(row)
    return l
def PrintVedioRCList(RCList):
    for item in RCList:
        print(item[0])
        print("    |__path %s" %item[4])
        print(" ")

def ListRepeatRC(DBName) :
    l = []
    l = GetHashList()
    sizeCount = 0 
    for h in l:
        lh = []
        lh.append(h)
        ret = GetFileByHash(lh)
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
    conn.close()
def ShowCount():
    for row in conn.execute(''' SELECT count(*) FROM srclib'''):
        print(row)

def test():
    ListRepeatRC(DBName)
if __name__ == "__main__" :
    ShowCount()
