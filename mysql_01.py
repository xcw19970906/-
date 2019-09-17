import pymysql
#1连接数据库
db = pymysql.connect(host="localhost",
                     port = 3306,
                     user='root',
                     password='123456',
                     database='marathon',
                     charset ='utf8')

#2获取游标对象
cur = db.cursor()

#3执行语句
sql = "insert into marathon values(4,'xiaohai','1997-09-06',18,'2019-09-16','2018-01-02 09:02:52','02:56:36');"
cur.execute(sql) #执行语句没提交

#4提交数据库
db.commit()

#5关闭游标
cur.close()

#关闭数据库
db.close()
