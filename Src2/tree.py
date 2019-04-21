import uuid
from enum import Enum

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
        self.inode = None
        self.dev = None
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