from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def DojoSurvey():
    return render_template('survey.html')

@app.route('/results', methods=['POST'])
def index():
    Name = request.form['name']
    Dojo_Location = request.form['city']
    Language = request.form['language']
    Comments = request.form['comments']
    return render_template('results.html', Name=request.form['name'], Dojo_Location=request.form['city'],Language=request.form['language'], Comments = request.form['comments'])

app.run(debug=True)
