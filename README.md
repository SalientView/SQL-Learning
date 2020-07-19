
**MySQL学习资源**
本资源以MySQL为目标，因为MySQL方面的文章已经有前人整理的非常到位，直接拿来用即可，不需要自己在重新整理，学习资源如下：

|	内容	|	地址	|
|	----	|	----	|	
|配置环境|https://www.jianshu.com/p/edca5142391c|
|测试题|https://zhuanlan.zhihu.com/p/53302593|
|在线写SQL|https://sqlzoo.net/<br>https://sqlbolt.com/<br>http://xuesql.cn/<br>http://sqlfiddle.com/<br>https://leetcode-cn.com/|
|关于SQL语句的执行顺序|https://zhuanlan.zhihu.com/p/48048479<br>https://www.cnblogs.com/yyjie/p/7788428.html<br>https://zhuanlan.zhihu.com/p/63299573|



**Python连接数据库**

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
