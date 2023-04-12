# AGENDA: Call CalcBMI on inputs, Call ClassifyBMI on CalcBMI's result
# requires import of files
# 

from flask import Flask, render_template, request
from app import app
 
@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        vals = request.form.getlist('BMI_params')
        feet = int(vals[0])
        inches = int(vals[1])
        pounds = int(vals[2])
        result = feet + inches + pounds
        return render_template('data.html', feet=feet, inches=inches, pounds=pounds, result=result)
 

# from flask import Flask, request, render_template_string
# from app import app

# @app.route('/', methods=['GET', 'POST'])
# @app.route('/index', methods=['GET', 'POST'])
# def index():

#     if request.method == 'POST':
#         vals = request.form.getlist('daily_calories')
#         val1 = float(vals[0])
#         val2 = float(vals[1])
#         result = val1 + val2
#     else:
#         val1 = ''
#         val2 = ''
#         result = ''

#     return render_template_string('''
# <form action="/" method="POST">
# <p>Input 1: <input type="number" name="daily_calories" value="{{ val1 }}"></p>
# <p>Input 2: <input type="number" name="daily_calories" value="{{ val2 }}"></p>
# <input type="submit" value="Calculate">
# <p>Result: <input type="number" name="result_dc" value="{{ result }}"></p>
# </form>
# ''', val1=val1, val2=val2, result=result)
