import sys
import os

IS_INIT = 0X01
IS_ERROR = 0X02

if __name__ == "__main__":
    param_num = len(sys.argv) 
    state = 0
    repo_name = "ShowLib"

    if param_num == 1:
        pass
    elif param_num == 3:
        if sys.argv[1] == "-i":
            repo_name = sys.argv[2]
            is_init = True
        elif sys.argv[1] == "-a":
            pass
        else:
            state &= IS_ERROR
    else:
        state &= IS_ERROR
    
    if state&IS_ERROR is True:
        print("sys exit")
    elif state&IS_INIT is True:
        if os.path.exists(repo_name) is False:
            os.makedirs(repo_name)
            os.makedirs(repo_name+os.sep+'.showlib')
        else:
            print("repo has existed!")
        print('init '+ repo_name + 'success')
    print("process exit!")