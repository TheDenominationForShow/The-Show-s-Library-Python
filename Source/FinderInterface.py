import sqlite3
DBName = 'h.db'
conn = sqlite3.connect(DBName)
c = conn.cursor()
def ListRepeatRC():
   
    c.execute('''''')
    conn.commit()
    conn.close()

def GetHashList() :
    l = []
    for row in conn.execute('SELECT distinct hash FROM srclib'):
        l.append(row[0])
    return l

def GetFileByHash(h) :
    l = []
    for row in conn.execute(''' SELECT * FROM srclib where hash = ? ''',h):
        l.append(row)
    return l

def test() :
    l = []
    l = GetHashList()
    for h in l:
        lh = []
        lh.append(h)
        ret = GetFileByHash(lh)
        if len(ret) > 1:
            print('hash is %s num is %d' %(h,len(ret)))
            print('=========================================')
            for item in ret:
                print("FileName %s" %item[0])
                print("    |__size %s" %item[2])
                print("    |__Path %s" %item[4])
                print('')
            print('')

test()
conn.close()


if __name__ == "__main__" :
    test()