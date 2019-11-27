'''
@author:jzf
@date: 2019-11-23 21:57
@desc: 配置模块
'''

import xml.dom.minidom as XmlDom
import os
import time
import datetime
import uuid
from sys import argv
config_version_1 = "1.0.0"
current_config_version = config_version_1
Broker_struct_version_1 = "1.0.0"
current_Broker_struct_version = Broker_struct_version_1

class Broker_struct:
    def __init__(self):
        self.ver = "1.0.0"
        self.uuid = None
        self.ip = None
        self.port = None

class SL_Config():
    def __init__(self, path):
        self.ver = "1.0.0"
        self.role = "storage"
        self.uuid = None
        self.mtime = None
        self.ctime = None
        self.brokers = []
        self.path =  os.path.abspath(path) + os.sep+"config.xml"

    def __del__(self):
        print('SL_Config close')

    def Load_config(self,fullpath = None):
        if fullpath != None:
            self.path = fullpath
        if os.path.exists(self.path) != True:
            return False
        else:
            doc = XmlDom.parse(self.path)
            root = doc.getElementsByTagName('root')[0]
            if root.attributes["ver"].value != current_config_version:
                return False
            self.ctime = root.getElementsByTagName('ctime')[0].firstChild.data
            self.mtime = root.getElementsByTagName('mtime')[0].firstChild.data
            storage_node = root.getElementsByTagName('storage')[0]
            self.uuid = storage_node.attributes["uuid"].value
            self.role = storage_node.attributes["role"].value
            if self.role == "broker":
                broker = Broker_struct()
                broker.ip = storage_node.getElementsByTagName('ip')[0].firstChild.data
                broker.port = storage_node.getElementsByTagName('port')[0].firstChild.data
                self.brokers.append(broker)
            brokers_node = root.getElementsByTagName('brokers')[0]
            broker_nodes = brokers_node.getElementsByTagName('broker')
            for item in broker_nodes:
                if item.attributes["ver"].value != current_Broker_struct_version:
                    continue
                broker = Broker_struct()
                broker.uuid = item.attributes["uuid"].value
                broker.ip = item.getElementsByTagName('ip')[0].firstChild.data
                broker.port = item.getElementsByTagName('port')[0].firstChild.data
                self.brokers.append(broker)
            return True
    def Create_config(self,role = "client"):
        doc = XmlDom.Document()
        root_node = doc.createElement('root')
        doc.appendChild(root_node)
        root_node.attributes["ver"] = current_config_version

        ctime_node = doc.createElement('ctime')
        mtime_node = doc.createElement('mtime')
        storage_node = doc.createElement('storage')
        brokers_node = doc.createElement('brokers')
        root_node.appendChild(ctime_node)
        root_node.appendChild(mtime_node)        
        root_node.appendChild(storage_node)
        root_node.appendChild(brokers_node)

        time_ctime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ctime_text_node = doc.createTextNode(time_ctime)
        ctime_node.appendChild(ctime_text_node)
        mtime_text_node = doc.createTextNode(time_ctime)
        mtime_node.appendChild(mtime_text_node)

        storage_node.attributes["uuid"] = str(uuid.uuid1())
        storage_node.attributes["role"] = role
        if role == "broker":
            ip = doc.createElement('ip')
            port = doc.createElement('port')
            storage_node.appendChild(ip)
            storage_node.appendChild(port)
            ip_text_node = doc.createTextNode("23.105.207.122")
            ip.appendChild(ip_text_node)
            port_text_node = doc.createTextNode("50051")
            port.appendChild(port_text_node)
        with open(self.path,'w',encoding="utf-8") as f:
            f.write(doc.toxml())

if __name__ == "__main__" :
  # 使用xx.py xxx路径
    old = datetime.datetime.now()
    print(old.strftime('%Y-%m-%d %H:%M:%S.%f'))  
    f = SL_Config(argv[1])
    if argv[2] == "Create_config":
        # 扫描文件夹
        f.Create_config("borker")
    elif argv[2] == "Load_config":
        f.Load_config()
        pass
    else:
        print("不能存在方法 "+argv[2]+",您可以利用当前代码自行编写脚本")
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    print(datetime.datetime.now()-old)

    