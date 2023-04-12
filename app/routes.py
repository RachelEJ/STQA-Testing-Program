# NOTE: form.html is not responding
# /index contains a paragraph tag
# /test contains the working form
# /form won't display at all
# /data contains the correct results

from flask import Flask, render_template, request
from app.BMI.BMIsystem import CalcBMI, ClassifyBMI
from app import app
 
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return "The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        vals = request.form.getlist('BMI_params')
        feet = int(vals[0])
        inches = int(vals[1])
        pounds = int(vals[2])
        result = CalcBMI(feet, inches, pounds)
        
        categoryNum = ClassifyBMI(result)
        if (categoryNum == 1):
            category = "underweight"
        elif (categoryNum == 2):
            category = "normal weight"
        elif (categoryNum == 3):
            category = "overweight"
        elif (categoryNum == 4):
            category = "obese"
        else:
            category = "ERROR"

        return render_template('data.html', feet=feet, inches=inches, pounds=pounds, result=result, category=category)