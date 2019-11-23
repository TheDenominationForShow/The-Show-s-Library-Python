import sqlite3


with open("H:\\番号知识厂商的编号方式及含义_files\\artrightadsogou300.html",'rb') as f:
    while True:
        block = f.read(1024)  
        if block:
            print(block)
        else:
            []