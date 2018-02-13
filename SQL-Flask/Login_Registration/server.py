from flask import Flask, redirect, render_template, session, request, flash
from mysqlconnection import MySQLConnector
import md5

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask (__name__)
app.secret_key = 'thesecretkey'
mysql = MySQLConnector(app,'login_registration')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration', methods=['POST'])
def registration():
    first_name = request.form['first_name'] #define variables inputed from form
    last_name = request.form['last_name']
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    confirm_password = md5.new(request.form['confirm_password']).hexdigest()
    valid = True
    if first_name == "": #Test via conditionals for different errors in each category
        flash("first_name must have at least three letters")
        valid = False
    elif len(first_name) < 3:
        flash("first_name must be longer than three characters")
        valid = False

    if last_name == "":
        flash("last_name must have at least three letters")
        valid = False
    elif len(first_name) < 3:
        flash("first_name must be longer than three characters")
        valid = False

    if email == "":
        flash("email cannot be empty and in a valid format")
        valid = False
    elif not EMAIL_REGEX.match(email):
        flash("email must be in valid format")
        valid = False

    if password == "":
        flash("password cannot be empty")
        valid = False
    elif confirm_password != password:
        flash("confirm password must match password")
        valid = False

    if valid == True: #send to data base
        query = "INSERT INTO users(first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password)"

        data = {
                'first_name':first_name,
                'last_name':last_name,
                'email':email,
                'password':password,
                }

        mysql.query_db(query, data)
        flash('success, please login')
        return redirect('/')
    elif valid == False:
        return redirect('/')

    return "You're registered"

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    query = "SELECT * FROM users WHERE email=:email"
    data = {
            "email":email,
    }
    user = mysql.query_db(query, data)
    if len(email) == 0:
        flash("this isn't a real user")
        return redirect('/')
    else:
        user = user[0]
        if user[0]["password"] == password:
            flash("Yay login success")
            return redirect('/success')
        else:
            flash("Invalid password")
            return redirect('/')


    return "You're logged in"

@app.route('/success')
def success():
    return "Success"

app.run(debug=True)
