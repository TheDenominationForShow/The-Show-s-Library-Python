 # -*- coding: UTF-8 -*-
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
from sl_signature import SL_Signature
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
        msg = "SL_Server initailize success"
        print(msg)
        self.logger.info(msg)
        return True

    def start(self):
        self.logger.info('SL_Server start')
        #启动
        self.run()
        pass
    def stop(self):
        self.logger.info('SL_Server stop')

    def command(self,request, context):
        if request.header.command == SL_Command.cmd_hello.value:
            #握手
            msg = "SL_Command.cmd_hello.value" + " id=" +request.header.localid
            self.logger.info(msg)
            print("SL_Command.cmd_hello.value")
            header = ShowLibInterface_pb2.MsgHeader(localid="",peerid="",command = 0)
            header.senssionid = request.header.senssionid
            header.peerid = request.header.localid
            if request.header.peerid != self.cfg.uuid:
                header.command = SL_Command.cmd_hello_deny.value
                return ShowLibInterface_pb2.CommandMsg(header = header,hash=[])
            header.command = SL_Command.cmd_empty.value
            header.localid = self.cfg.uuid
            return ShowLibInterface_pb2.CommandMsg(header = header,hash=[])
        elif request.header.command == SL_Command.cmd_request.value:
            #来自客户端的请求会话
            print("SL_Command.cmd_request")
            header = ShowLibInterface_pb2.MsgHeader(localid="",peerid="",command = 0)
            header.senssionid = request.header.senssionid
            if request.header.peerid != self.cfg.uuid:
                header.peerid = request.header.localid
                header.command = SL_Command.cmd_empty.value
                return ShowLibInterface_pb2.CommandMsg(header = header,hash=[])
            res = None
            self.lock.acquire()
            for i in range(0,len(self.l)):
                if self.l[i].header.localid == request.header.localid:
                    res = self.l.pop(i)
                    print(res)
                    break
            self.lock.release()
            if res != None:
                msg = "SL_Command.cmd_request" + " id=" +request.header.localid + " rescommand ="+str(res.header.command)
                self.logger.info(msg)
                res.header.peerid = request.header.localid
                res.header.localid =  self.cfg.uuid
                return ShowLibInterface_pb2.CommandMsg(header = res.header,hash = res.hash)
            else:
                return ShowLibInterface_pb2.CommandMsg(header = header,hash = [])
        elif request.header.command == SL_Command.cmd_publish_RCHashCount.value:
            #
            pass
        elif request.header.command == SL_Command.cmd_publish_RCHashRecords.value:
            self.lock.acquire()
            print(request)
            self.l.append(request)
            self.lock.release()
        elif request.header.command == SL_Command.cmd_subcribe_RCHash.value:
            pass
        elif request.header.command == SL_Command.cmd_subcribe_Storage.value:
            self.lock.acquire()
            print(request)
            self.l.append(request)
            self.lock.release()
        elif request.header.command == SL_Command.cmd_publish_RC.value:
            pass
        else:
            print("暂未实现")
            pass
        header = ShowLibInterface_pb2.MsgHeader(localid="",peerid="",command = 0)
        header.senssionid = request.header.senssionid
        header.peerid = request.header.localid   
        header.command = SL_Command.cmd_empty.value
        header.localid = self.cfg.uuid       
        print(header)     
        return ShowLibInterface_pb2.CommandMsg(header = header,hash=[])
    def InsertRCHashRecords(self, request_iterator, context):
        pass
    def PulishRCHashCount(self,request, context):
        pass
    def PulishRCHashRecords(self, request_iterator, context):
        sendheader = ShowLibInterface_pb2.MsgHeader()
        recordset = []
        for item in request_iterator:
            #sg = SL_Signature(self.rootdir,item.header.localid)
            for rec in item.record:
                record = []
                record.append(rec.name)
                record.append(rec.hash)
                record.append(rec.size)
                #sg.InsertToDB(record)
                recordset.append(record)
            sendheader.senssionid = item.header.senssionid
            sendheader.localid = self.cfg.uuid
            sendheader.peerid = item.header.localid
            sendheader.command = SL_Command.cmd_empty.value
        self.InsertDB_Signature_Records(recordset,item.header.localid)
        self.InsertDB_Signature_Records(recordset)
        return ShowLibInterface_pb2.CommandMsg(header = sendheader,hash=[])
    def GetRCHashCount(self,request, context):
        pass
    def GenRecord(self,req):
        sendheader = ShowLibInterface_pb2.MsgHeader()
        sendheader.senssionid = req.header.senssionid
        sendheader.localid = self.cfg.uuid
        sendheader.peerid = req.header.localid
        sendheader.command = req.header.command
        sg = SL_Signature(self.rootdir)
        ls = sg.GetRecords()
        msg = "GetRCHashRecords" + " id=" +req.header.localid + " len="+str(len(ls))
        self.logger.info(msg)
        for i in range(0,len(ls)):
            retl = []
            size = str(ls[i][2])
            re = ShowLibInterface_pb2.RCHashRecord(hash = ls[i][1], name = ls[i][0],size = size )
            retl.append(re)
            yield ShowLibInterface_pb2.RCHashRecords(header = sendheader, record = retl)
    def GetRCHashRecords(self,request, context):
        iter = self.GenRecord(request)
        return  iter 
    def DownLoadRC(self,request, context):
        pass
    def UpLoadRC(self, request_iterator, context):
        pass
    def run(self):
        if len(self.cfg.brokers) == 0:
            print("broker配置错误，请到配置文件中添加")
            msg = "SL_Client thread start failed！"
            print(msg)
            self.logger.info(msg)
            return False
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
            for record in records:
                if item[1] == record[1]:
                    bexsit = True
                    self.logger.info("hash exsit name=%s hash =%s" %(item[0],item[1]))
                    break
            if  bexsit == True:
                continue
            records.append(tuple(item[0:3]))
        sg.InsertDB_Records(records)
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
        print("不存在方法 "+argv[2]+",您可以利用当前代码自行编写脚本" )
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    print(datetime.datetime.now()-old)