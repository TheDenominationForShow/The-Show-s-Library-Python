'''
@author:jzf
@date: 2019-11-23 21:57
@desc: 服务端模块
'''
from concurrent import futures
import os
import time
import logging
import datetime
from sys import argv
from sl_config import SL_Config,Broker_struct
import grpc
from sl_rpc import SL_Command
import ShowLibInterface_pb2
import ShowLibInterface_pb2_grpc

import threading,queue

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
class SL_Server(ShowLibInterface_pb2_grpc.showlibifServicer):
    def __init__(self, rootdir, DBName=None):
        self.logger = logging.getLogger("Server")
        fileHandler = logging.FileHandler(
            filename='Server.log', encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fileHandler.setFormatter(formatter)
        self.logger.addHandler(fileHandler)
        self.logger.setLevel(logging.INFO)
        self.rootdir = os.path.abspath(rootdir)
        self.storage = None
        self.cfg = None
        self.lock = threading.Lock()
        self.l = []
    def __del__(self):
        print('SL_Server close')
    def initailize(self):
        self.logger.info('SL_Server initailize')
        cfg_path = self.rootdir + os.sep + ".showlib"
        if not os.path.exists(cfg_path): 
            os.mkdir(cfg_path)
            self.logger.info('makedir '+ cfg_path)
        #加载配置文件
        self.cfg = SL_Config(cfg_path)
        if self.cfg.Load_config() != True:
            self.cfg.Create_config(role = "broker")
        if self.cfg.Load_config() != True:
            print("ShowLib load config failed! exit")
            self.logger.error('SL_Server initailize load config failed！')
            return False
        #扫描
        print("SL_Server initailize success")
        return True

    def start(self):
        self.logger.info('SL_Server start')
        #启动
        self.run()
        pass
    def stop(self):
        self.logger.info('SL_Server stop')

    def command(self,request, context):
        if request.command == SL_Command.cmd_hello.value:
            #握手
            header = ShowLibInterface_pb2.MsgHeader(localid="",peerid="",command = 0)
            header.senssionid = request.header.senssionid
            if request.header.peerid != self.cfg.uuid:
                header.peerid = request.header.localid
                header.command = SL_Command.cmd_hello_deny.value
                return ShowLibInterface_pb2.CommandMsg(header = header,hash=[])
            header.command = SL_Command.cmd_empty.value
            return ShowLibInterface_pb2.CommandMsg(header = header,hash=[])
        elif request.command == SL_Command.cmd_request.value:
            header = ShowLibInterface_pb2.MsgHeader(localid="",peerid="",command = 0)
            header.senssionid = request.header.senssionid
            if request.header.peerid != self.cfg.uuid:
                header.peerid = request.header.localid
                header.command = SL_Command.cmd_empty.value
                return ShowLibInterface_pb2.CommandMsg(header = header,hash=[])
            res = None
            self.lock.acquire()
            for item in self.l:
                if item.header.localid == request.header.localid:
                    res = item
                    l.remove(item)
                    break
            self.lock.release()
            if res != None:
                res.header.peerid = request.header.localid
                res.header.localid =  self.cfg.uuid
                return ShowLibInterface_pb2.CommandMsg(header = res.header,hash = res.hash)
            else:
                print("=,=")
                return ShowLibInterface_pb2.CommandMsg(header = header,hash = [])
        elif request.command == SL_Command.cmd_publish_RCHashCount.value:
            #
            pass
        elif request.command == SL_Command.cmd_publish_RCHashRecords.value:
            self.lock.acquire()
            self.l.append(request)
            self.lock.release()
        elif request.command == SL_Command.cmd_subcribe_RCHash.value:
            pass
        elif request.command == SL_Command.cmd_subcribe_Storage.value:
            self.lock.acquire()
            self.l.append(request)
            self.lock.release()
        elif request.command == SL_Command.cmd_publish_RC.value:
            pass
        else:
            print("暂未实现")
            pass

    def InsertRCHashRecords(self, request_iterator, context):
        pass
    def PulishRCHashCount(self,request, context):
        pass
    def PulishRCHashRecords(self, request_iterator, context):
        for item in request_iterator:
            sg = SL_Signature(self.rootdir,item.header.peerid)
            records = []
            for rec in res.record:
                record = []
                record.append(res.record.name)
                record.append(res.record.hash)
                record.append(res.record.size)
                records.append(record)
            sg.InsertToDB(records)
        sendheader = ShowLibInterface_pb2.MsgHeader()
        sendheader.senssionid = res.header.senssionid
        sendheader.localid = self.cfg.uuid
        sendheader.peerid = res.header.localid
        sendheader.command = int(res.header.cmd_empty.value)
        return ShowLibInterface_pb2.CommandMsg(header = sendheader,hash=[])
    def GetRCHashCount(self,request, context):
        pass
    def GenRecord(self,req):
        sendheader = ShowLibInterface_pb2.MsgHeader()
        sendheader.senssionid = req.header.senssionid
        sendheader.localid = self.cfg.uuid
        sendheader.peerid = res.header.localid
        sendheader.command = int(res.header.cmd_request.value)
        sg = SL_Signature(self.rootdir)
        ls = sg.GetRecord()
        for i in range(0,len(ls)):
            retl = []
            size = str(ls[i][2])
            ShowLibInterface_pb2.RCHashRecord(hash = ls[i][1], name = ls[i][0],size = size )
            retl.append()
            yield ShowLibInterface_pb2.RCHashRecords(header = sendheader, record = retl)
    def GetRCHashRecords(self,request, context):
        iter = self.GenRecord(self,req)
        return  iter 
    def DownLoadRC(self,request, context):
        pass
    def UpLoadRC(self, request_iterator, context):
        pass
    def run(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        ShowLibInterface_pb2_grpc.add_showlibifServicer_to_server(self, server)
        connectStr = self.cfg.brokers[0].ip+":"+self.cfg.brokers[0].port
        print(connectStr)
        server.add_insecure_port(connectStr)
        server.start()
        try:
            while True:
                time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
            server.stop(0)
            self.stop()
if __name__ == "__main__" :
    # 使用xx.py xxx路径
    old = datetime.datetime.now()
    print(old.strftime('%Y-%m-%d %H:%M:%S.%f'))  
    f = SL_Server(argv[1])
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