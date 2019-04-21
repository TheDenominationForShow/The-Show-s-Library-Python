'''
仓库的文件树
'''
import os
import datetime
import hashlib
from enum import Enum
from tree import TreeNode, DirNode, FileNode

def GetFileHash( FileName ) :
	hs = hashlib.sha256()
	with open(FileName,'rb') as f:
		byte = f.read(512)
		hs.update(byte)
	return hs.hexdigest()

class NODE_DIFF_TYPE(Enum):
    SAME = 0
    DIFF_NAME = 0x01
    DIFF_INODE = 0X02
    DIFF_SIZE = 0X04
    DIFF_SUBDIR = 0X08
    DIFF_MTIME = 0X10
    DIFF_RELPATH = 0X20

def setTreeNodeFsStat(treeNode, absPath):
    stat_result = os.stat(absPath)
    treeNode.ctime = stat_result.st_ctime
    treeNode.mtime = stat_result.st_mtime
    treeNode.size = stat_result.st_size
    treeNode.dev = stat_result.st_dev
    treeNode.inode = stat_result.st_ino

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
                newNode.hash = GetFileHash(tmp)
            else:
                #如果是路径
                newNode = DirNode(item)
                curDirNode.subNodes.append(newNode)
                pathStack.append(newNode)
            newNode.relPath = os.path.relpath(tmp, repoBasePath)
            setTreeNodeFsStat(newNode,tmp)

def diff_DirNode(newDirNode, oldDirNode):
    ret = NODE_DIFF_TYPE.SAME
    if newDirNode.inode != oldDirNode.inode:
        ret |= NODE_DIFF_TYPE.DIFF_INODE
    if newDirNode.mtime != oldDirNode.mtime:
        ret |= NODE_DIFF_TYPE.DIFF_MTIME
    if newDirNode.size != oldDirNode.size:
        ret |= NODE_DIFF_TYPE.DIFF_SIZE
    if newDirNode.relPath != oldDirNode.relPath:
        ret |= NODE_DIFF_TYPE.DIFF_RELPATH
    return ret

def test_tree():
    pathStack = []
    pathStack.append(root)
    while len(pathStack) != 0:
        curDirNode = pathStack.pop(0) 
        print(curDirNode.name)
        for item in curDirNode.subNodes:
            pathStack.append(item) 
        for obj in curDirNode.objects:
            print(obj)
            print ('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))
if __name__ == "__main__":

    old = datetime.datetime.now()
    print(old.strftime('%Y-%m-%d %H:%M:%S.%f'))
    createTree()
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    print((datetime.datetime.now()-old))
    old = datetime.datetime.now()
    print(old.strftime('%Y-%m-%d %H:%M:%S.%f'))
    test_tree()
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    print((datetime.datetime.now()-old))
    