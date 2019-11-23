import xml.dom.minidom as XmlDom
import os
import time
import datetime
import uuid
from sys import argv

def TimeStampToTime(timestamp):
	timeStruct = time.localtime(timestamp)
	return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)
config_version = "1.0.0"
class SL_Config():
    def __init__(self, path):
        self.path =  os.path.abspath(path) + os.sep+"config.xml"
    def __del__(self):
        print('SL_Config close')
    def Load_config(self,fullpath = None):
        if path != None:
            self.path = fullpath
        if os.path.exists(path):
            pass
        else:
            pass
    def Create_config(self,role):
        doc = XmlDom.Document()

        root_node = doc.createElement('root')
        doc.appendChild(root_node)
        root_node.attributes["ver"] = config_version

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
        
        with open(self.path,'w') as f:
            f.write(doc.toxml())

if __name__ == "__main__" :
  # 使用xx.py xxx路径
    old = datetime.datetime.now()
    print(old.strftime('%Y-%m-%d %H:%M:%S.%f'))  
    f = SL_Config(argv[1])
    if argv[2] == "Create_config":
        # 扫描文件夹
        f.Create_config("borker")
    elif argv[2] == "ShowRepeatHashRC":
        #显示重复
        pass
    else:
        print("不能存在方法 "+argv[2]+",您可以利用当前代码自行编写脚本")
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    print(datetime.datetime.now()-old)

    