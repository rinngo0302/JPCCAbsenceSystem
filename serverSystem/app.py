from flask import Flask, render_template, request
import sqlite3
import jinja2

from user import User
from dataBase import checkUser, addDBData

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
        user = checkUser(request.form["name"], request.form["pass"])
        
        if user != False:
            print("id: {0}\nname: {1}\npassword: {2}".format(user.id, user.name, user.password))
            return render_template("home.html", \
                username = user.name, \
                userid = user.id)
        else:
            return render_template("login_error.html")
    else:
        return "ERROR"

@app.route('/login/home/addDBDate', methods=["GET"])
def addData():
    if request.method == "GET":
        userid = request.args["userid"]
        fullYear = request.args["fullYear"]
        month = request.args["month"]
        date = request.args["date"]
        print("{0}/{1}/{2}".format(fullYear, month, date))
        addDBData(userid, fullYear, month, date)
        return "succeed"
    else:
        return "ERROR"