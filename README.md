# The-Show-s-Library-Python
The-Show-s-Library for python
## 说明
最近守教图书馆陷入了低潮期，没事就写个py版本的玩一玩

setup.py 暂时还不需要去写，另外 

## 使用
* 首先配置python环境
    * 安装python3
    * 
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