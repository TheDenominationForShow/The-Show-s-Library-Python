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
import grpc

import ShowLibInterface_pb2
import ShowLibInterface_pb2_grpc
from sl_rpc import SL_Command
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
        with grpc.insecure_channel(self.cfg.brokers[0].ip+":"+self.cfg.brokers[0].port) as channel:
            stub = ShowLibInterface_pb2_grpc.showlibifStub(channel)
            header = ShowLibInterface_pb2.MsgHeader()
            header.senssionid = 0
            header.localid = self.cfg.uuid
            header.peerid = self.cfg.brokers[0].uuid
            header.command = int(SL_Command.cmd_hello.value)
            l = []
            l.append("")
            response = stub.command(ShowLibInterface_pb2.CommandMsg(header = header,hash = l))
        #线程接收

        pass
    def stop(self):
        self.logger.info('SL_Client stop')
    def run(self):
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