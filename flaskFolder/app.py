# File containing Flask webpage setup

from flask import Flask, render_template, request
from flaskFolder.BMI.BMIsystem import CalcBMI, ClassifyBMI

app = Flask(__name__)

@app.route('/')
@app.route('/index', methods = ['POST', 'GET'])

# HOME PAGE
def index():
    # reads data after the POST request
    if request.method == 'POST':

        # stores values from the input elements
        feet = int(request.form.get('feetInput'))
        inches = int(request.form.get('inchesInput'))
        pounds = int(request.form.get('poundsInput'))

        # calculates and classifies BMI
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

        # renders page using template and data from above
        return render_template('index.html', feet=feet, inches=inches, pounds=pounds, result=result, category=category)
    else:
        # renders page using template and no data
        return render_template('index.html')

if __name__ == "__main__":
    app.run()