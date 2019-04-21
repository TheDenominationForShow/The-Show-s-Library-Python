'''
仓库的文件树
'''
import os
import uuid
from enum import Enum
import datetime

class NodeTypeEnum(Enum):
    DIR = 0
    FILE = 1

class TreeNode:
    def __init__(self, name, parentNode=None):
        self.uuid = uuid.uuid1()
        # 节点名称
        self.name = name
        # 节点类型
        self.type = NodeTypeEnum.DIR
        # 子节点为 文件夹或者文件
        self.parentNode = parentNode
        # 如果创建和修改时间相同是不是说明是同一个文件夹  
        self.mtime = None
        self.ctime = None
        self.size = None
        self.relPath = '.'

class DirNode(TreeNode):
    def __init__(self, name):
        TreeNode.__init__(self, name)
        self.subNodes = []
        self.objects = []

class FileNode(TreeNode):
    def __init__(self, name):
        TreeNode.__init__(self, name)
        self.type = NodeTypeEnum.FILE
        self.hash = None

root = DirNode("repoName")    
def createTree():     
    repoBasePath = os.path.realpath('.')
    root.relPath = '.'
    pathStack = []
    pathStack.append(root)
    while len(pathStack) != 0:
        curDirNode = pathStack.pop(0)  
        curPath = os.path.join(repoBasePath, curDirNode.relPath)
        curPath = os.path.realpath(curPath)
        print('curpath   ' +curPath)
        subList = os.listdir(curPath)
        for item in subList:
            tmp = os.path.join(curPath, item)        
            print(tmp)
            newNode = None
            if os.path.isfile(tmp) is True:
                newNode = FileNode(item)
                root.objects.append(newNode)
            else:
                #如果是路径
                newNode = DirNode(item)
                curDirNode.subNodes.append(newNode)
                pathStack.append(newNode)
            newNode.relPath = os.path.relpath(tmp, repoBasePath)
            newNode.ctime = os.path.getctime(tmp)
            newNode.mtime = os.path.getmtime(tmp)
            newNode.size = os.path.getsize(tmp)

if __name__ == "__main__":

    old = datetime.datetime.now()
    print(old.strftime('%Y-%m-%d %H:%M:%S.%f'))
    createTree()
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    print((datetime.datetime.now()-old))
    
