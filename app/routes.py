from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        vals = request.form.getlist('daily_calories')
        val1 = float(vals[0])
        val2 = float(vals[1])
        result = val1 + val2
    else:
        val1 = ''
        val2 = ''
        result = ''

    return render_template_string('''
<form action="/" method="POST">
<p>Input 1: <input type="number" name="daily_calories" value="{{ val1 }}"></p>
<p>Input 2: <input type="number" name="daily_calories" value="{{ val2 }}"></p>
<input type="submit" value="Calculate">
<p>Result: <input type="number" name="result_dc" value="{{ result }}"></p>
</form>
''', val1=val1, val2=val2, result=result)
