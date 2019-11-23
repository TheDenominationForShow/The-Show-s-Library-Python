
import xml.dom.minidom as XmlDocument
 
#定义XML文档对象
doc=XmlDocument.Document()
#创建根节点
xUsers=doc.createElement('users')
doc.appendChild(xUsers)
 
#添加用户1
xUser=doc.createElement('user')
xUsers.appendChild(xUser)
xUser.attributes['id']='1'
 
xUsername=doc.createElement('username')
xUser.appendChild(xUsername)
xUsername.appendChild(doc.createTextNode('admin'))
 
xEmail=doc.createElement('email')
xUser.appendChild(xEmail)
xEmail.appendChild(doc.createTextNode('admin@qq.com'))
 
xAge=doc.createElement('age')
xUser.appendChild(xAge)
xAge.appendChild(doc.createTextNode('23'))
 
#添加用户2
xUser=doc.createElement('user')
xUsers.appendChild(xUser)
xUser.attributes['id']='2'
 
xUsername=doc.createElement('username')
xUser.appendChild(xUsername)
xUsername.appendChild(doc.createTextNode('user'))
 
xEmail=doc.createElement('email')
xUser.appendChild(xEmail)
xEmail.appendChild(doc.createTextNode('user@qq.com'))
 
xAge=doc.createElement('age')
xUser.appendChild(xAge)
xAge.appendChild(doc.createTextNode('22'))
 
#添加用户3
def addUser(id,username,email,age):
    xUser=doc.createElement('user')
    xUsers.appendChild(xUser)
    xUser.attributes['id']=id
 
    xUsername=doc.createElement('username')
    xUser.appendChild(xUsername)
    xUsername.appendChild(doc.createTextNode(username))
 
    xEmail=doc.createElement('email')
    xUser.appendChild(xEmail)
    xEmail.appendChild(doc.createTextNode(email))
 
    xAge=doc.createElement('age')
    xUser.appendChild(xAge)
    xAge.appendChild(doc.createTextNode(age))
 
for i in range(3,10):
    addUser(str(i),'user3','admin@qq.com','13')
 
#保存
with open('test2.xml','w') as f:
    
    f.write(doc.toxml())