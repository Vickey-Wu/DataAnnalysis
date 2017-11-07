#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2017/11/5 18:09 
# @name: connect_mysql
# @author：vickey-wu

import MySQLdb
# db = MySQLdb.connect("10.10.10.5","root","123456","test")
db = MySQLdb.connect("127.0.0.1","encrypt_name","encrypt_passwd")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用execute方法执行SQL语句
cursor.execute("SHOW DATABASES")
# 使用 fetchone() 方法获取一条数据。
# data = cursor.fetchone()
# 使用 fetchall() 方法获取全部数据。
data = cursor.fetchall()
print data
db.close()
