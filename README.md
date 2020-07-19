
**连接数据库参数如下**

| 参数名称| 含义| 参数取值类型| 
| ------ | ------ |------ |
| host| 数据库服务器地址|string| 
| port| MySQL连接端口 |int|
| db| 数据库名称 |string|
| user| 用户名 |string|
| password| 密码 |string|




```
import pymysql

connection = pymysql.connect(host='localhost', 
                             port=3306, 
                             user='root', 
                             password='123', 
                             db='learn_use',
                             charset='utf8')

try:
    with connection.cursor() as cursor:
    
        sql1 = "SELECT count(*) FROM stu"
        sql2 = "SELECT * FROM stu "

        cursor.execute(sql1)
        rows = cursor.fetchall() 
        
        cursor.execute(sql2)
        stu_data = cursor.fetchall() 

finally:
    connection.close()

print('rows of data:',rows)
print('data:\n',stu_data)
```
