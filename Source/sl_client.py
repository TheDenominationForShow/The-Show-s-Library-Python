'''
@author:jzf
@date: 2019-11-23 21:57
@desc: 客户端模块
'''
import os
import time
import logging
import datetime
from sys import argv
from sl_storage import SL_Storage
from sl_config import SL_Config,Broker_struct
from sl_signature import SL_Signature
import grpc

import ShowLibInterface_pb2
import ShowLibInterface_pb2_grpc
from sl_rpc import SL_Command
import threading,queue

class SL_Client:
    def __init__(self, rootdir, DBName=None):
        self.logger = logging.getLogger("Client")
        fileHandler = logging.FileHandler(
            filename='Client.log', encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s -[%(thread)d] - %(levelname)s: %(message)s  -[%(filename)s:%(lineno)d]")
        fileHandler.setFormatter(formatter)
        self.logger.addHandler(fileHandler)
        self.logger.setLevel(logging.INFO)
        self.rootdir = os.path.abspath(rootdir)
        self.storage = None
        self.cfg = None
        self.run_flag = False
        self.queue = queue.Queue(maxsize=4096)
        self.threadrecv = None
        self.thread_process = None
    def __del__(self):
        print('SL_Client close')
    def initailize(self):
        self.logger.info('SL_Client initailize')
        cfg_path = self.rootdir + os.sep + ".showlib"
        if not os.path.exists(cfg_path): 
            os.mkdir(cfg_path)
            self.logger.info('makedir '+ cfg_path)
        #加载配置文件
        self.cfg = SL_Config(cfg_path)
        if self.cfg.Load_config() != True:
            self.cfg.Create_config()
        if self.cfg.Load_config() != True:
            print("ShowLib load config failed! exit")
            self.logger.error('SL_Client initailize load config failed！')
            return False
        #扫描
        self.storage = SL_Storage(self.rootdir)
        old = datetime.datetime.now()
        msg = "ShowLib scan storage start   " + old.strftime('%Y-%m-%d %H:%M:%S.%f')
        print(msg)
        self.logger.info(msg)
        records = self.storage.scan_path()
        now = datetime.datetime.now()
        msg = "ShowLib scan storage end    " + now.strftime('%Y-%m-%d %H:%M:%S.%f')+ "  耗时"+ str(now-old)
        print(msg)
        self.logger.info(msg)
        msg = "新扫描仓库资源 count =" + str(len(records))
        print(msg)
        self.logger.info(msg)
        msg = "旧仓库资源 count =" + str(self.storage.ShowRecordsCount())
        print(msg)
        self.logger.info(msg)
        #存storageDB
        old = datetime.datetime.now()
        self.storage.InsertDB_Records(records)
        now = datetime.datetime.now()
        msg = "insert to storageDB " + now.strftime('%Y-%m-%d %H:%M:%S.%f')+ "  耗时"+ str(now-old)
        print(msg)
        self.logger.info(msg)
        #存signatureDB
        old = datetime.datetime.now()
        self.storage.InsertDB_Signature_Records(records)
        now = datetime.datetime.now()
        msg = "insert to signatureDB " + now.strftime('%Y-%m-%d %H:%M:%S.%f')+ "  耗时"+ str(now-old)
        print(msg)
        self.logger.info(msg)

        msg = "SL_Client initailize success"
        print(msg)
        self.logger.info(msg)
        return True

    def start(self):
        self.logger.info('SL_Client start')
        #向服务器推送
        if len(self.cfg.brokers) == 0:
            print("没有可用的broker连接，请到配置文件中添加")
            msg = "SL_Client thread start failed！"
            print(msg)
            self.logger.info(msg)
            return False
        connectStr = self.cfg.brokers[0].ip+":"+self.cfg.brokers[0].port
        print(connectStr)
        try:
            with grpc.insecure_channel(connectStr) as channel:
                stub = ShowLibInterface_pb2_grpc.showlibifStub(channel)
                sendheader = ShowLibInterface_pb2.MsgHeader()
                sendheader.senssionid = 2
                sendheader.localid = self.cfg.uuid
                sendheader.peerid = self.cfg.brokers[0].uuid
                sendheader.command = SL_Command.cmd_hello.value
                l = []
                print(sendheader)
                response = stub.command(ShowLibInterface_pb2.CommandMsg(header = sendheader,hash = l),timeout=20)
                if response.header.command == SL_Command.cmd_hello_deny.value:
                    msg = "cmd_hello_deny error id = " +(self.cfg.brokers[0].uuid)
                    print(msg)
                    self.logger.error(msg)
                    return Falsel.append()
                sendheader.command = SL_Command.cmd_subcribe_Storage.value
                print(sendheader)
                response = stub.command(ShowLibInterface_pb2.CommandMsg(header = sendheader,hash = l),timeout=20)
                sendheader.command = SL_Command.cmd_publish_RCHashRecords.value
                print(sendheader)
                response = stub.command(ShowLibInterface_pb2.CommandMsg(header = sendheader,hash = l),timeout=10)
        except grpc._channel._Rendezvous as egrpc:
            self.logger.error(egrpc.details)
            self.logger.error(egrpc.debug_error_string)
            msg = "SL_Client start Failed"
            print(msg)
            self.logger.info(msg)
            return False
        except Exception as e:
            print(e)
            self.logger.info(e)
            msg = "SL_Client start Failed"
            print(msg)
            self.logger.info(msg)
            return False
        msg = "SL_Client thread start "
        print(msg)
        self.logger.info(msg)
        #线程接收
        self.run_flag = True
        self.threadrecv = threading.Thread(target=self.recv)
        self.thread_process = threading.Thread(target=self.process)
        self.threadrecv.start()
        self.thread_process.start()
        msg = "SL_Client start success"
        print(msg)
        self.logger.info(msg)
        return True
    def stop(self):
        print("-------SL_Client stopping-----")
        self.run_flag = False
        if self.thread_process is not None:
            self.thread_process.join()
            self.threadrecv.join()
        self.logger.info('SL_Client stop')
        print("SL_Client stop")
    def recv(self):
        msg = "recv start"
        #print(msg)
        self.logger.info(msg)
        #向服务器询问是否有事件需要处理
        last_command = SL_Command.cmd_empty.value
        while self.run_flag:
            try:
                connectStr = self.cfg.brokers[0].ip+":"+self.cfg.brokers[0].port
                with grpc.insecure_channel(connectStr) as channel:
                    stub = ShowLibInterface_pb2_grpc.showlibifStub(channel)
                    sendheader = ShowLibInterface_pb2.MsgHeader()
                    sendheader.senssionid = 0
                    sendheader.localid = self.cfg.uuid
                    sendheader.peerid = self.cfg.brokers[0].uuid
                    sendheader.command = int(SL_Command.cmd_request.value)
                    response = stub.command(ShowLibInterface_pb2.CommandMsg(header = sendheader,hash = []))
                    if response.header.command != last_command:
                        self.logger.info("recv command.value = "+str(response.header.command))
                        last_command = response.header.command
                        pass
                    if response.header.command != SL_Command.cmd_empty.value:
                        self.queue.put(response)
            except grpc._channel._Rendezvous as egrpc:
                self.logger.error(egrpc.details)
                self.logger.error(egrpc.debug_error_string)
            except Exception as e:
                print(e)
                self.logger.info(e)
                msg = "SL_Client recv Exception"
                print(msg)
                self.logger.info(msg)
        self.logger.info("recv end")
    def process(self):
        self.logger.info("process start")
        process_status = True #work
        while self.run_flag:
            connectStr = self.cfg.brokers[0].ip+":"+self.cfg.brokers[0].port
            with grpc.insecure_channel(connectStr) as channel:
                stub = ShowLibInterface_pb2_grpc.showlibifStub(channel)
                try:
                    while self.queue.empty() != True:
                        process_status = True
                        res = self.queue.get()
                        if res.header.command == SL_Command.cmd_publish_RCHashRecords.value:
                            #print("cmd_publish_RCHashRecords")
                            self.logger.info("process_status cmd_publish_RCHashRecords")
                            #处理本地发布
                            self.PulishRCHashRecords(stub,res)
                            pass
                        elif res.header.command == SL_Command.cmd_subcribe_Storage.value:
                            self.logger.info("process_status cmd_subcribe_Storage")
                            #处理本地订阅
                            self.GetRCHashRecords(stub,res)
                            #print("cmd_subcribe_Storage")
                            pass
                        else:
                            print("暂未实现")
                except grpc._channel._Rendezvous as egrpc:
                    self.logger.error(egrpc.details)
                    self.logger.error(egrpc.debug_error_string)
                except Exception as e:
                    print(e)
                    #self.logger.error(e.msg)
            if self.queue.empty() == True:
                if process_status:
                    self.logger.info("process_status sleep")
                    process_status = False
                time.sleep(10)
        self.logger.info("process end")
    def InsertRCHashRecords(self, stub, res):
        pass
    def PulishRCHashCount(self, stub, res):
        pass
    def Get_local_SignatureRecord(self):
        sg = SL_Signature(self.rootdir)
        print("GetRecord "+str(threading.currentThread().ident))
        ls = sg.GetRecords()
        return ls
    def GetRecord(self,res):
        sendheader = ShowLibInterface_pb2.MsgHeader()
        sendheader.senssionid = res.header.senssionid
        sendheader.localid = self.cfg.uuid
        sendheader.peerid = res.header.localid
        sendheader.command = res.header.command
        ls = self.Get_local_SignatureRecord()
        for i in range(0,len(ls)):
            retl = []
            #因为是sqlite，基本入库自动转换
            size = str(ls[i][2])
            retl.append(ShowLibInterface_pb2.RCHashRecord(name = ls[i][0],hash = ls[i][1],size = size ))
            yield ShowLibInterface_pb2.RCHashRecords(header = sendheader, record = retl)

    def PulishRCHashRecords(self, stub, res):
        iter = self.GetRecord(res)
        respoense = stub.PulishRCHashRecords(iter)
        print(respoense)

    def GetRCHashCount(self, stub, res):
        pass
    def InsertDB_Signature_Records(self, recordset,dbname = None):
        if len(recordset) == 0:
            return
        records = []
        sg = SL_Signature(self.rootdir,dbname)
        hash_list = sg.GetHashList()
        for item in recordset:
            # name hash size
            bexsit = False
            for hash in hash_list:
                if item[1] == hash:
                    bexsit = True
                    self.logger.info("hash exsit name=%s hash =%s" %(item[0],item[1]))
                    break
            if  bexsit == True:
                continue
            hash_list.append(tuple(item))
            records.append(tuple(item))
        sg.InsertDB_Records(records)
    def GetRCHashRecords(self, stub, res):
        records = []
        respoense = stub.GetRCHashRecords(res)
        dbname = None
        for item in respoense:
            '''
            records = []
            for rec in item.record:
                record = []
                record.append(rec.name)
                record.append(rec.hash)
                record.append(rec.size)
                records.append(record)
            sg.InsertToDB(records)
            '''
            dbname = item.header.localid
            for rec in item.record:
                record = []
                record.append(rec.name)
                record.append(rec.hash)
                record.append(rec.size)
                records.append(record)
        if len(records) == 0:
            return  
        self.InsertDB_Signature_Records(records,dbname)
        #sg = SL_Signature(self.rootdir,dbname)
        #print("GetRCHashRecords Threadid="+str(threading.currentThread().ident))
        #for it in records:
        #    sg.InsertToDB(it)
        print("GetRCHashRecords end "+str(threading.currentThread().ident))
    def DownLoadRC(self, stub, res):
        pass
    def UpLoadRC(self, stub, res):
        pass
if __name__ == "__main__" :
    # 使用xx.py xxx路径
    old = datetime.datetime.now()
    print(old.strftime('%Y-%m-%d %H:%M:%S.%f'))  
    f = SL_Client(argv[1])
    if argv[2] == "initailize":
        # 初始化
        f.initailize()
    elif argv[2] == "start":
        f.initailize()
        f.start()
        run_flag = True
        while run_flag:
            stop = input("输入 stop 停止:")
            if stop == "stop":
                f.stop()
                run_flag = False
            else:
                print("未知命令")
    else:
        print("不能存在方法 "+argv[2]+",您可以利用当前代码自行编写脚本" )
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    print(datetime.datetime.now()-old)