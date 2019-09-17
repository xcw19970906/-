
''''''
'''
读操作
'''
import pymysql
#1连接数据库
db = pymysql.connect(
                     user='root',
                     password='123456',
                     database='marathon',
                     charset ='utf8')
#2获取游标
cur = db.cursor()


#3获取数据
sql = "select * from marathon where age > 20;"
cur.execute(sql)  #提交给数据库


#4可以直接遍历游标
for i in cur:   #就相当于蹙额里面存放的就是满足where条件的
    print(i)

#1获取一个查询结果
# one_row = cur.fetchall()
# print(one_row)


#2获取多个查询结果
# many_row = cur.fetchall(2)
# print(many_row)

#3获取所有查询结果
# all_row = cur.fetchall()
# print(all_row)

cur.close()
db.close()
