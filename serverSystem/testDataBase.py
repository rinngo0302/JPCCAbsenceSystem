############### name と password でデータベースでユーザーを取得する。 ###############

import sqlite3

conn = sqlite3.connect("Data/user.db")
cur = conn.cursor()

cur.execute('select * from user where name="太郎" and password="taro"')
items = cur.fetchall()
print("All Data: {0}".format(items))

if items == []:
    print("要素はありませんでした")
else:
    for i in range(len(items)):
        if (items[i][0] != None):
            id = items[i][0]
            name = items[i][1]
            password = items[i][2]
            print("id: {0}\nname: {1}\npassword: {2}".format(id, name, password))
            break