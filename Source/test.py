'''
仓库的文件树
'''
import uuid
from enum import Enum

class NodeTypeEnum(enum):
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

    def getFullPath():
        l_path = []
        pathStr = ""
        l_path.append(self.name)
        parentNode = self.parentNode
        while(parentNode != None):
            l_path.append(parentNode.name)
            parentNode = parentNode.parentNode
        l_path.remove[0]
        l_path.reverse()
        for item in l_path:
            pathStr+=item
            pathStr+="/"
        return pathStr

class DirNode(TreeNode):
    def __init__(self, name):
        TreeNode.__init__(name)
        self.subNodes = []
        self.objects = []

class FileNode(TreeNode):
    def __init__(self, name):
        TreeNode.__init__(name)
        self.type = NodeTypeEnum.FILE
        self.hash = None

class RepoTree:
   
    def __init__(self, repo):
        self.repo = repo
        self.treeRoot = self.DirNode(repo.name)
        self.curNode = self.treeRoot
    def __del__(self):
        pass
    def initTree():
        for root, dirs, files in os.walk(self.repo.path):

            pathStr =self.repo.path+"\\" +self.curNode.getFullPath()
            if os.path.samefile(pathStr,root) is False:
                self.curNode =   
            self.curNode.name = os.path.basename(root)
            for item in dirs:
                tmp = DirNode(item)
                self.curNode.subNodes.append(tmp)
                tmp.mtime = os.path.getmtime()
                tmp.ctime = os.path.getctime()
                tmp.size = os.path.getsize()
            for item in files:
                tmp = FileNode(item)
                tmp.mtime = os.path.getmtime()
                tmp.ctime = os.path.getctime()
                tmp.size = os.path.getsize()
                self.curNode.subNodes.append(tmp)
    def searchNodeByPath():
        for 
    #这是一个绝对路径
    repoBasePath
    os.listdir
if __name__ == "__main__":
    a = RepoTree("hehe")