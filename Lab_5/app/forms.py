from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange, Length

class CodeExecutionForm(FlaskForm):
    code = StringField('Code', validators=[DataRequired(), Length(min=1)])
    timeout = IntegerField('Timeout', validators=[DataRequired(), NumberRange(min=1, max=30)])
