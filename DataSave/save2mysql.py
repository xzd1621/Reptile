import pymysql

# db=pymysql.connect(host='localhost',user='root',password='123456',port=3306)
# cursor=db.cursor()
# cursor.execute('select version()')
# data=cursor.fetchone()
# print('Database version:',data)
# cursor.execute("create database spiders default character set utf8")
# db.close()

#创建表格
# db=pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spiders')
# cursor=db.cursor()
# sql='create table students (' \
#     'id varchar(255) not null ,' \
#     'name varchar (255) not null ,' \
#     'age int not null ,' \
#     'primary key (id))'
# cursor.execute(sql)
# db.close()

#插入数据
id='20120001'
user='Bob'
age=20
db=pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spiders')
cursor=db.cursor()
sql='insert into students(id,name,age) values (%s,%s,%s)'
try:
    cursor.execute(sql,(id,user,age))
    db.commit()
except:
    db.rollback()
db.close()
