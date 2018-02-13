from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/') #page with nothing but "No Nijas Here"
def noturtle():
    return "No Ninjas Here!"

@app.route('/ninja') #Page with pictures of all the Ninja Turtles
def ninjaturtles():
    return render_template('allninjas.html')

@app.route('/ninja/<ninja_color>') #Route to html for specific Turtle
def singleturtle(ninja_color):
    if (ninja_color == "purple" or ninja_color == "blue" or ninja_color == "orange" or ninja_color == "red"):
        return render_template(ninja_color+'.html')
    else:
        return render_template('non_ninja.html')


app.run(debug=True)
