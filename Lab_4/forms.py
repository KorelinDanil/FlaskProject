from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange, Optional, Length
from validators import phone_length

class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[
        DataRequired(message="Email is required"),
        Email(message="Invalid email format")
    ])
    phone = IntegerField("Phone", validators=[
        DataRequired(),
        phone_length(10, 10, message="Phone must be exactly 10 digits")
    ])

    name = StringField("Name", validators=[DataRequired(message="Name is required")])
    address = StringField("Address", validators=[DataRequired(message="Address is required")])
    index = IntegerField("Index", validators=[DataRequired(message="Index is required")])
    comment = StringField("Comment", validators=[Optional()])



