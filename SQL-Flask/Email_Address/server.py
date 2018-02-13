from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask (__name__)
app.secret_key = 'safeemail'
mysql = MySQLConnector(app,'myemail')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/email', methods=['POST'])
def email_check():

    if len(request.form['email_address']) < 1:
        flash("Invalid Email Address")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email_address']):
        flash("Invalid Email Address")
        return redirect('/')
    else:
        query = "INSERT INTO email (email_address, created_at) VALUES (:email_address, now())"

        data = {
                 'email_address': request.form['email_address']
               }

        mysql.query_db(query, data)

    return redirect('/success')
@app.route('/success', methods=['GET'])
def email_list():
    query = "SELECT * FROM email"
    email = mysql.query_db(query)
    return render_template('success.html', all_address=email)

app.run(debug=True)
