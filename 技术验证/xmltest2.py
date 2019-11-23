
import xml.dom.minidom as XmlDocument
 
#加载文件到内存
doc=XmlDocument.parse('test.xml')
#根节点users
xUsers=doc.getElementsByTagName('users')
if xUsers and len(xUsers)>0:
    #读取user节点迭代式
    xUserList=xUsers[0].getElementsByTagName('user')
    for user in xUserList:
        #读取属性id
        id=user.attributes['id'].value
        print('user id: ',id)
 
        #读取用户名
        xUsername=user.getElementsByTagName('username')
        if xUsername and len(xUsername)>0:
            username=xUsername[0].firstChild.data
            print('user name: ',username)
 
        #读取电子邮箱
        xEmail=user.getElementsByTagName('email')
        if xEmail and len(xEmail)>0:
            email=xEmail[0].firstChild.data
            print('email: ',email)
 
        #读取年龄
        xAge=user.getElementsByTagName('age')
        if xAge and len(xAge)>0:
            age=xAge[0].firstChild.data
            print('age: ',age)