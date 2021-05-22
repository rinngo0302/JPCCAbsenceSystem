import sqlite3
from flask import request
import os

from user import User
from date import Date

def checkUser(name, password): # データベースに接続し、そのユーザーがいるかを確認する
    conn = sqlite3.connect("Data/DataBase/user.db")
    cur = conn.cursor()

    cur.execute('select * from userList where name="{0}" and password="{1}"'.format(name, password)) # フィルタを使って確認
    items = cur.fetchall()
    print("All Data: {0}".format(items))
    conn.close()

    if items == []:
        print("要素はありませんでした")
        return False
    else:
        for i in range(len(items)): # ユーザーのデータを取得
            if (items[i][0] != None):
                user = User()
                user.id = items[i][0]
                user.name = items[i][1]
                user.password = items[i][2]
                user.category = items[i][3]
                print("id: {0}\nname: {1}\npassword: {2}\ncategory: {3}".format(user.id, user.name, user.password, user.category))
                return user

def makeDB(id):
    file = open("Data/dataBase/userAttendedDate/{0}.db".format(id))
    conn = sqlite3.connect("Data/dataBase/userAttendedDate/{0}.db".format(id))

    cur = conn.corsor()
    cur.execute("drop table if exists attendedDate;")
    cur.execute("create table attendedDate (fullYear integer not null, month integer not null, date integer not null);")

    conn.commit()
    conn.close()
    file.close()

def addDBData(userid, fullYear, month, date):
    conn = sqlite3.connect("Data/DataBase/userAttendedDate/{0}.db".format(userid))
    cur = conn.cursor()

    cur.execute('insert into attendedDate (fullYear, month, date) values ({0}, {1}, {2});'.format(fullYear, month, date))
    
    conn.commit()
    conn.close()

def getLastDate(userid): # 前回のデータを取得
    conn = sqlite3.connect("Data/DataBase/userAttendedDate/{0}.db".format(userid))
    cur = conn.cursor()

    cur.execute("SELECT * FROM attendedDate WHERE ROWID IN ( SELECT max( ROWID ) FROM attendedDate );")
    item = cur.fetchall()

    if item == []:
        print("過去のデータはありませんでした。")
        return False
    else:
        FULL_YEAR = 0
        MONTH = 1
        DATE = 2
        print(item[0][0])
        print(item[0][1])
        print(item[0][2])
        
        date = Date(item[0][FULL_YEAR], item[0][MONTH], item[0][DATE])

        return date

def getHasPaidMoney(userid):
    conn = sqlite3.connect("Data/DataBase/money.db")
    cur = conn.cursor()

    cur.execute("select * from money")
    item = cur.fetchall()

    hasPaidMoney = item[int(userid - 2)][1]

    return hasPaidMoney