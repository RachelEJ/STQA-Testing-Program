from flask import Flask, render_template, request
from BMI.BMIsystem import CalcBMI, ClassifyBMI

app = Flask(__name__)

@app.route('/')
@app.route('/index', methods = ['POST', 'GET'])

def index():
    if request.method == 'POST':
        feet = int(request.form.get('feetInput'))
        inches = int(request.form.get('inchesInput'))
        pounds = int(request.form.get('poundsInput'))
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

        return render_template('index.html', feet=feet, inches=inches, pounds=pounds, result=result, category=category)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()