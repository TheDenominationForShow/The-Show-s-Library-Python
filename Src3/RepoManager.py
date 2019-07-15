
from finder import Finder 
import os

class RepoManager:
    def __init__(self, repo_name):
        self.repo_name = repo_name
        self.repo_name_file = repo_name+os.sep+'.showlib'
        self.initRepo()
        self.finder = Finder(os.path.realpath(self.repo_name_file))
        pass
    def __del__(self):  
        pass

    def initRepo(self):
        if os.path.exists(self.repo_name) is False:
            os.makedirs(self.repo_name)
            os.makedirs(self.repo_name_file)
            
    def addItem2Repo(self,src):
        pass
