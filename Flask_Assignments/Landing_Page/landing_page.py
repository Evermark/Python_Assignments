from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def root():
    return "Hello Welcome to the Information Server for a Coding Dojo Student"
@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')
@app.route('/dojos')
def dojos():
    return render_template('dojos.html')

app.run(debug=True)
