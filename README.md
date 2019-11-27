# The-Show-s-Library-Python
The-Show-s-Library for python
## 说明
最近守教图书馆陷入了低潮期，没事就写个py版本的玩一玩

setup.py 暂时还不需要去写，另外 

## 使用
### 具体步骤
* 首先配置python环境
    * 安装python3 version >= 3.5
    * 安装 gRPC依赖:
        * python -m pip install grpcio  
        * python -m pip install grpcio-tools 这个用来安装protobuf
* 下载 `git clone 本项目.git`，并进入到Souce目录
* 启动命令 `python  sl_client.py "库目录" "start"`  第一次扫描可能会慢，之后都是轻量增加文件都是飞速的
* 输入 `stop` 等待退出

### 配置

目前还不咋支持，仅仅调通了签名的传输

```xml
<?xml version="1.0" ?>
<!--root根节点，属性ver 本次配置文件版本-->
<root ver="1.0.0">
    <!--ctime 仓库创建时间-->
    <ctime>2019-11-23 22:45:06</ctime>
    <!--mtime 仓库修改时间-->
    <mtime>2019-11-23 22:45:06</mtime>
    <!--storage 仓库节点  role 仓库角色 broker或者client  uuid 仓库的唯一标识-->
    <storage role="client" uuid="d76039a2-0dff-11ea-8dc6-9eb6d0fd43ad" />
    <!--brokers borker列表节点-->
    <brokers>
        <!--broker borker节点  uuid broker仓库的唯一标识  ver broker版本-->
        <broker uuid="da165114-0eb4-11ea-bc40-aaaa00147a10" ver="1.0.0">
            <!--ip ip节点  broker监听ip-->
            <ip>23.105.207.122</ip>
            <!--port port节点  broker监听端口-->
            <port>50051</port>
        </broker>
    </brokers>
</root>
```

## 遗留

之后使用 sl_storage.py脚本进行操作，命令大致为  sl_storage.py "文件路径" "调用方法"

* sl_storage.py "G:\\图书馆" "scan"  扫描文件夹，生成索引库必须先走这一步

* sl_storage.py "G:\\图书馆" "ShowRepeatHashRC 显示签名相同的资源，统计冗余文件占用

## 性能

* 今天550个g的视频和图片，扫描了接近两个小时，推算效率为5g/min----80m/s（`约为机械移动磁盘性能瓶颈`），所以仓库太大，第一次初始化会比较慢。
    * `但是普通的pdf资源完全没问题哦`

sudo nohup python -u sl_server.py "." "start" > nohup.out 2>&1 &
Generate gRPC code
python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/helloworld.proto
python -m grpc_tools.protoc -I.  --python_out=.  --grpc_python_out=.  ShowLibInterface.proto
> 今天扫描照片库，大约4g的大小，2400个文件。耗时11分钟，平均每秒6m

* ShowLib scan storage end    2019-11-25 23:42:27.906408  耗时0:11:58.923699
    (2438,)
* 11-25 23：53 对比使用git测试
    * 23：59 git add * 结束
    * 23：59 git commit -am "init" 的瞬间结束，现在0：00
    * git使用中，任务管理器读取显示几kb，写入12m/s，这个太奇葩了吧
* 11-26 10:58 笔记本电脑 5200转 3代i5 8g内存
    * 原始版本 扫描杂项文件 大小7.3g,数目2000，耗时10min  ShowLib scan storage end    2019-11-26 10:57:23.088592  耗时0:10:37.492650 (2002,)
    * mmap版本 耗时13min，什么鬼？    ShowLib scan storage end    2019-11-26 11:26:21.387161  耗时0:13:39.674971 (2002,)
    * mmap版本                      ShowLib scan storage end    2019-11-26 11:47:40.668895  耗时0:15:57.902134 (2002,)
    * 原始版本                      ShowLib scan storage end     2019-11-26 12:08:18.360124  耗时0:17:50.305137 (2002,)
    * git 启动时间13:28 停止时间 13:36 耗时8分钟
    * sha1版本                          ShowLib scan storage end    2019-11-26 13:51:09.816232  耗时0:10:45.188610(2002,)
    * no sqlite                         ShowLib scan storage end    2019-11-26 13:56:05.029213  耗时0:01:56.525342 (0,)
    * no sqlite                         ShowLib scan storage end    2019-11-26 14:04:03.453133  耗时0:01:57.722534 (0,
    * no sqlite && sha1 ShowLib         ShowLib scan storage end    2019-11-26 14:06:56.842025  耗时0:01:57.891734(0,)
    * no sqlite && sha1 && mmap         ShowLib scan storage end    2019-11-26 14:13:42.983007  耗时0:02:12.974503 (0,)
## 测试

在客户端生成的config.xml `brokers`中添加下测试borker `23.105.207.122` 重启即可进行签名的上传和下载
```xml
<brokers>
    <broker uuid="08660846-0e61-11ea-bb3b-d89ef3948ae4" ver="1.0.0">
        <ip>23.105.207.122</ip>
        <port>50051</port>
    </broker>
</brokers>
```