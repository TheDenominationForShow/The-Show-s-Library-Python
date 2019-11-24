
'''
@author:jzf
@date: 2019-11-24 21:57
@desc: rpc协议模块
'''
from enum import Enum

class SL_Command(Enum):
    
    # 握手失败
    cmd_hello_deny = -1
    # 本次会话，什么都不用做
    cmd_empty = 0
    # 握手
    cmd_hello = 1
    # 发布仓库签名数
    cmd_publish_RCHashCount = 2
    # 发布仓库签名
    cmd_publish_RCHashRecords = 3
    # 通过订阅资源
    cmd_subcribe_RCHash = 4
    # 订阅仓库签名
    cmd_subcribe_Storage = 5
    # 发布资源
    cmd_publish_RC = 6
       # 询问
    cmd_request = 7