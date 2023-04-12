from flask import render_template, flash, redirect, request, render_template_string
from app import app
# from app.form import BMIForm


@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        vals = request.form.getlist('BMI_params')
        val1 = int(vals[0])
        val2 = int(vals[1])
        val3 = int(vals[2])
        result = val1 + val2 + val3
        # result = CalcBMI(val1, val2, val3)
    else:
        val1 = ''
        val2 = ''
        val3 = ''
        result = ''

    return render_template_string('''
        <form action="/" method="POST">
        <p>Input 1: <input type="number" name="BMI_params" value="{{ val1 }}"></p>
        <p>Input 2: <input type="number" name="BMI_params" value="{{ val2 }}"></p>
        <p>Input 3: <input type="number" name="BMI_params" value="{{ val3 }}"></p>
        <input type="submit" value="Calculate">
        <p>Result: <input type="number" name="result_dc" value="{{ result }}"></p>
        </form>
        ''', val1=val1, val2=val2, val3=val3, result=result)

    # return render_template('index.html', title='BMI System' valFeet=valFeet, valInches=valInches, valPounds=valPounds)

    
    # form = BMIForm()
    # if form.validate_on_submit():
    #     flash('Validation requested for feet = {}, inches = {}, weight = {}'.format(
    #         form.feet.data, form.inches.data, form.pounds.data))

    #     return redirect('/index') # change to /result later
    # return render_template('index.html', title='BMI System', form=form)

@app.route('/result', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int)
    var_2 = request.form.get("var_2", type=int)
    operation = request.form.get("operation")
    if(operation == 'Addition'):
        result = var_1 + var_2
    elif(operation == 'Subtraction'):
        result = var_1 - var_2
    elif(operation == 'Multiplication'):
        result = var_1 * var_2
    elif(operation == 'Division'):
        result = var_1 / var_2
    else:
        result = 'INVALID CHOICE'
    entry = result
    return render_template('result.html', entry=entry)