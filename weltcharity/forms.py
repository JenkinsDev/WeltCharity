from flask_wtf import Form
from wtforms import BooleanField, TextField, PasswordField, validators
from datetime import timedelta


class RegistrationForm(Form):
    username = TextField('Username:', [validators.Length(min=5, max=35)])
    email = TextField('Email Address:', [validators.Length(min=0, max=255), validators.Email()])
    password = PasswordField('Password:', [validators.InputRequired(), validators.EqualTo('password_conf', message='Passwords must match')])
    password_conf = PasswordField('Password Confirmation:', [validators.InputRequired()])

class LoginForm(Form):
    username_or_email = TextField('Username or Email Address:', [validators.InputRequired()])
    password = PasswordField('Password:', [validators.InputRequired()])
