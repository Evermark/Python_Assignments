from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "My_little_Secret"

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/count', methods = ['POST'])
def counter():
    session['view'] +=1
    return redirect('/')
app.run(debug=True)
