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
        * python -m pip install grpcio  一般只安装这个就行
        * python -m pip install grpcio-tools
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

## 测试

在客户端生成的config.xml `brokers`中添加下测试borker `23.105.207.122` 重启即可进行签名的上传和下载
```xml
<brokers>
    <broker uuid="da165114-0eb4-11ea-bc40-aaaa00147a10" ver="1.0.0">
        <ip>23.105.207.122</ip>
        <port>50051</port>
    </broker>
</brokers>
```