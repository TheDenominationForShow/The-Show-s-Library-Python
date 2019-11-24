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
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
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
        self.storage.scan_path()
        now = datetime.datetime.now()
        msg = "ShowLib scan storage end    " + now.strftime('%Y-%m-%d %H:%M:%S.%f')+ "  耗时"+ str(now-old)
        print(msg)
        self.logger.info(msg)
        msg = "仓库资源 count =" + str(self.storage.ShowRecordsCount())
        print(msg)
        self.logger.info(msg)
        print("SL_Client initailize success")
        return True

    def start(self):
        self.logger.info('SL_Client start')
        #向服务器推送
        connectStr = self.cfg.brokers[0].ip+":"+self.cfg.brokers[0].port
        print(connectStr)
        with grpc.insecure_channel(connectStr) as channel:
            stub = ShowLibInterface_pb2_grpc.showlibifStub(channel)
            sendheader = ShowLibInterface_pb2.MsgHeader()
            sendheader.senssionid = 0
            sendheader.localid = self.cfg.uuid
            sendheader.peerid = self.cfg.brokers[0].uuid
            sendheader.command = int(SL_Command.cmd_hello.value)
            response = stub.command(ShowLibInterface_pb2.CommandMsg(header = sendheader,hash = []))
            if response.header.command == SL_Command.cmd_hello_deny.value:
                msg = "cmd_hello_deny error id = " +(brokers[0].uuid)
                print(msg)
                self.logger.error(msg)
                return False
        #线程接收
        self.run_flag = True
        self.threadrecv = threading.Thread(target=recv)
        self.thread_process = threading.Thread(target=process)
        self.threadrecv.start()
        self.thread_process.start()
        return True
    def stop(self):
        self.logger.info('SL_Client stop')
    def recv(self):
        #向服务器询问是否有事件需要处理
        while self.run_flag:
            time.sleep(2*60)
            connectStr = self.cfg.brokers[0].ip+":"+self.cfg.brokers[0].port
            with grpc.insecure_channel(connectStr) as channel:
                stub = ShowLibInterface_pb2_grpc.showlibifStub(channel)
                sendheader = ShowLibInterface_pb2.MsgHeader()
                sendheader.senssionid = 0
                sendheader.localid = self.cfg.uuid
                sendheader.peerid = self.cfg.brokers[0].uuid
                sendheader.command = int(SL_Command.cmd_request.value)
                response = stub.command(ShowLibInterface_pb2.CommandMsg(header = sendheader,hash = []))
                if response.header.command != SL_Command.cmd_empty.value:
                    self.queue.put(response)

    def process(self):
         while self.run_flag:
            if self.queue.empty():
                time.sleep(2*60)
            connectStr = self.cfg.brokers[0].ip+":"+self.cfg.brokers[0].port
            with grpc.insecure_channel(connectStr) as channel:
                stub = ShowLibInterface_pb2_grpc.showlibifStub(channel)
                while self.queue.empty() != True:
                    res = self.queue.get()
                    if res.header.command == SL_Command.cmd_publish_RCHashRecords.value:
                        print("cmd_publish_RCHashRecords")
                        #处理本地发布
                        self.PulishRCHashRecords(stub,res)
                        pass
                    elif res.header.command == SL_Command.cmd_subcribe_Storage.value:
                        #处理本地订阅
                        self.GetRCHashRecords(stub,res)
                        print("cmd_subcribe_Storage")
                        pass
                    else:
                        print("暂未实现")
    
    def InsertRCHashRecords(self, stub, res):
        pass
    def PulishRCHashCount(self, stub, res):
        pass
    def GenRecord(self,res):
        sendheader = ShowLibInterface_pb2.MsgHeader()
        sendheader.senssionid = res.header.senssionid
        sendheader.localid = self.cfg.uuid
        sendheader.peerid = res.header.localid
        sendheader.command = int(res.header.cmd_request.value)
        sg = SL_Signature(self.rootdir)
        ls = sg.GetRecord()
        for i in range(0,len(ls)):
            retl = []
            size = str(ls[i][2])
            ShowLibInterface_pb2.RCHashRecord(name = ls[i][0],hash = ls[i][1],size = size )
            retl.append()
            yield ShowLibInterface_pb2.RCHashRecords(header = sendheader, record = retl)

    def PulishRCHashRecords(self, stub, res):
        iter = GenRecord()
        respoense = stub.PulishRCHashRecords(iter)
        print(respoense)
    def GetRCHashCount(self, stub, res):

    def GetRCHashRecords(self, stub, res):
        stub.GetRCHashRecords(res)
        for item in res:
            sg = SL_Signature(self.rootdir,res.header.peerid)
            record = []
            record.append(res.RCHashRecord.name)
            record.append(res.RCHashRecord.hash)
            record.append(res.RCHashRecord.size)
            sg.InsertToDB(record)
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
    else:
        print("不能存在方法 "+argv[2]+",您可以利用当前代码自行编写脚本" )
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    print(datetime.datetime.now()-old)