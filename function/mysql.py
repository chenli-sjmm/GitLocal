import pymysql

def select(database,select_sql):
    db = pymysql.connect(**database)
    sql = select_sql
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)
    return data

# #打开数据库连接
# #注意：这里已经假定存在数据库testdb，db指定了连接的数据库，当然这个参数也可以没有
# db = pymysql.connect(host='192.168.10.141', port=3306, user='sjmmuat', passwd='wVd9WPi3x4wIvKKG', db='sjmm_uat', charset='utf8')
# #使用cursor方法创建一个游标
# cursor = db.cursor()
# #查询数据库版本
#
# cursor.execute("select version()")
#
# data = cursor.fetchone()
#
# print(" Database Version:%s" % data)
#
# #创建数据库test
# cursor.execute("drop database if exists test")  #如果数据库已经存在，那么删除后重新创建
#
# sql = "create database test"
#
# cursor.execute(sql)
#
# #创建数据库表
#
# cursor.execute("drop table if exists employee")  #如果数据表已经存在，那么删除后重新创建
#
# sql = """
#
# CREATE TABLE EMPLOYEE (
#
# FIRST_NAME CHAR(20) NOT NULL,
#
# LAST_NAME CHAR(20),
#
# AGE INT,
#
# SEX CHAR(1),
#
# INCOME FLOAT )
#
# """
#
# cursor.execute(sql)
#
#
# #查询数据表数据
#
# sql = "select * from employee"
#
# cursor.execute(sql)
#
# data = cursor.fetchone()
#
# print(data)
#
#
# #插入数据
#
# sql = "insert into employee values ('李','梅',20,'W',5000)"
#
# cursor.execute(sql)
#
# db.commit()
#
# #查看插入后的结果
#
# sql = "select * from employee"
#
# cursor.execute(sql)
#
# data = cursor.fetchone()
#
# print(data)
#
# #指定条件查询数据表数据
#
# sql = " select * from employee where income > '%d' " % (1000)
#
# cursor.execute(sql)
#
# data = cursor.fetchone()
#
# print(data)
#
# #更新数据库
#
# sql = " update employee set age = age+1 where sex = '%c' " % ('W')
#
# cursor.execute(sql)
#
# db.commit()
#
# #查看更新后的结果
#
# sql = "select * from employee"
#
# cursor.execute(sql)
#
# data = cursor.fetchone()
#
# print(data)
#
#
# #删除数据
#
# sql = " delete from employee where age > '%d' " % (30)
#
# cursor.execute(sql)
#
# db.commit()
#
# #查看更新后的结果
#
# sql = "select * from employee"
#
# cursor.execute(sql)
#
# data = cursor.fetchone()
#
# print(data)
#
# # 关闭数据连接
# db.close()
#
# '''1、说明
#
# ·上例中"sql=..."语句，是经典的MySQL语句的形式，将数据库语句写在双引号内，形成类似字符串的形式；
#
# ·使用cursor对象的execute()方法具体执行数据库的操作；
#
# ·对于插入、更新、删除等操作，需要使用db.commit()来提交到数据库执行，对于查询、创建数据库和数据表的操作不需要此语句。
#
# 2、为有效避免因为错误导致的后果，使用以下方式来执行数据库的操作：'''
# try:
#
#   # 执行 SQL 语句
#
#   cursor.execute(sql)
#
#   # 提交修改
#
#   db.commit()
#
# except:
#
#   # 发生错误时回滚
#
#   db.rollback()