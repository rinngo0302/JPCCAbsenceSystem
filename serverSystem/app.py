from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')                                     # index.html
def index():
    return render_template("index.html")

@app.route('/login')                                # login.html
def login():
    return render_template("login.html")

@app.route('/login/home', methods=["GET", "POST"])  # home.html or login_error.html
def home():
    if request.method == "POST": # POST受信
        username = request.form["name"]
        password = request.form["pass"]
        if checkUser(username, password):
            return "{0} さん、お帰りなさい".format(username)
        else:
            return render_template("login_error.html")
    else:
        return "ERROR"

def checkUser(name, password):
    conn = sqlite3.connect("Data/DataBase/user.db")
    cur = conn.cursor()

    cur.execute('select * from userList where name="{0}" and password="{1}"'.format(name, password))
    items = cur.fetchall()
    print("All Data: {0}".format(items))

    if items == []:
        print("要素はありませんでした")
        return False
    else:
        for i in range(len(items)):
            if (items[i][0] != None):
                id = items[i][0]
                name = items[i][1]
                password = items[i][2]
                print("id: {0}\nname: {1}\npassword: {2}".format(id, name, password))
                return True