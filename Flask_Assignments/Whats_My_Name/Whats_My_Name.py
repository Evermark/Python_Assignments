from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def What_Name():
    return render_template('index.html')
@app.route('/process', methods=['POST'])
def Ur_Name():
    print request.form['name']
    return redirect('/')
app.run(debug=True)
