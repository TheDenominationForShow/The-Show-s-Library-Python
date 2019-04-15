'''
做什么
对路径 xxx 生成一个 yyy的仓库
'''
import uuid
import RepoTree
import os

class Respository:

    class RespositoryImpl:
        def __init__(self, name=None):
            self.uuid = uuid.uuid1()
            if name == None:
                self.name = "master"
            else:
                self.name = name
            self.path = ""
            pass

    def __init__(self):
        self.repo = self.RespositoryImpl()
        pass
    def __del__(self):
    #self.conn.close()
        pass
    def createRepo(self, path, name):
        self.repo.path = path
        self.repo.name = name
        self.tree = RepoTree(repo)
        #创建配置文件的路径
        #os.makedirs(path+"\\"+".ShowLib")
    
    def openRepo(self,path,name):
        pass
    def createTree(self):
        pass
    # 可以整个提交，也可以局部文件夹提交
    def Commit(self,path):
        pass

if __name__ == "__main__":
    a = Respository()
    a.createRepo("./Repotest","Repotest")
    
