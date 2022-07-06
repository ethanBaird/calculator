from flask import render_template
from app import app
from modules.calculator import Calculator

@app.route('/calculator')
def index():
    return render_template('index.html')

@app.route('/calculator/add/<n1>/<n2>')
def add_result(n1, n2):
    return render_template('result.html', result=Calculator(int(n1),int(n2)).add())

@app.route('/calculator/subtract/<n1>/<n2>')
def subtract_result(n1, n2):
    return render_template('result.html', result=Calculator(int(n1),int(n2)).subtract())

@app.route('/calculator/multiply/<n1>/<n2>')
def multiply_result(n1, n2):
    return render_template('result.html', result=Calculator(int(n1),int(n2)).multiply())

@app.route('/calculator/divide/<n1>/<n2>')
def divide_result(n1, n2):
    return render_template('result.html', result=Calculator(int(n1),int(n2)).divide())