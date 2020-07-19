import pymysql


connection = pymysql.connect(host='localhost', 
                             port=3306, 
                             user='root', 
                             password='123', 
                             db='learn_use',
                             charset='utf8')

try:
    with connection.cursor() as cursor:
    
        sql1 = "SELECT count(*) FROM sc"
        sql2 = "SELECT * FROM sc "

        cursor.execute(sql1)
        rows = cursor.fetchall() 
        
        cursor.execute(sql2)
        sc = cursor.fetchall() 

finally:
    connection.close()

# 查看数据
print('数据行数为:',rows,'\n前五行数据为:',sc)
