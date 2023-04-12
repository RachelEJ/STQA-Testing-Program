from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BMIForm(FlaskForm):
    feet = StringField('Feet', validators=[DataRequired()])
    inches = StringField('Inches', validators=[DataRequired()])
    pounds = StringField('Pounds', validators=[DataRequired()])
    submit = SubmitField('Calculate')