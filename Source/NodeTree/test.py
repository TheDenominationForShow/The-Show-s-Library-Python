import os
from enum import Enum

class NodeType(Enum):
    TYPE_EMPTY = 0
    TYPE_CLASS = 1
    TYPE_LEAF = 2

class Node:
    def __init__(self,ParentNode):
        self.type = NodeType.TYPE_EMPTY
        self.Cunrrent = None
        self.ParentNode = ParentNode
        self.SubNodes = []
    def __del__(self):
        pass
    def AddSubNode(self,SubNode):
        SubNode.ParentNode = self
        self.SubNodes.append(SubNode)
    #增加新的资源节点
    def AddNewRCSubNode(self):
        SubNode = Node(self)
        SubNode.type = NodeType.TYPE_LEAF
        SubNode.Cunrrent = ResourceObj()
        return SubNode
    #增加新的类节点
    def AddNewClassSubNode(self):
        SubNode = Node(self)
        SubNode.type = NodeType.TYPE_CLASS
        SubNode.Cunrrent = ClassObj()
        return SubNod

    def DelSubNode(self):
        pass

class ClassObj:
    def __init__(self,name):
        self.name = name
        self.comment = None
class ResourceObj:
    def __init__(self,name,hash,size,mtime)
        self.name = name 
        self.hash = hash
        self.size = size
        self.mtime = mtime

# 初始化一个仓库和树
def InitRepository(Root = None):
    if Root is None:
        Root = os.path.abspath('.')
    tree = Node(None)
    #增加资源节点
    newRCNode = tree.AddNewRCSubNode()
    newRCNode.Cunrrent.name = 
    newRCNode.Cunrrent.hash = 
    newRCNode.Cunrrent.size = 
    newRCNode.Cunrrent.mtime = 
    #增加类节点
    newClassNode = tree.AddNewClassSubNode()
    newClassNode.Cunrrent.name = 
    newClassNode.Cunrrent.comment =
#将树进行xml或者json格式的序列化


    
    

    
    