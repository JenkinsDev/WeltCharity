from flask_wtf import Form
from flask_wtf.html5 import EmailField, TelField
from wtforms import BooleanField, TextField, PasswordField, validators
from datetime import timedelta

import re


def validate_phone(form, field):
    result = re.match(r'1?\W*([2-9][0-8][0-9])\W*([2-9][0-9]{2})\W*([0-9]{4})(\se?x?t?(\d*))?', field.data)
    if len(field.data) > 0 and not result:
    	raise validators.ValidationError('Phone must be a valid phone number')


class RegistrationForm(Form):
    username = TextField('Username:', [validators.Length(min=5, max=35)])
    email = EmailField('Email Address:', [validators.Length(min=0, max=255), validators.Email()])
    password = PasswordField('Password:', [validators.InputRequired(), validators.EqualTo('password_conf', message='Passwords must match')])
    password_conf = PasswordField('Password Confirmation:', [validators.InputRequired()])


class LoginForm(Form):
    username_or_email = TextField('Username or Email Address:', [validators.InputRequired()])
    password = PasswordField('Password:', [validators.InputRequired()])


class GeneralAccountSettingsForm(Form):
    username = TextField('Username:', [validators.Length(min=5, max=35)])
    email = EmailField('Email Address:', [validators.Length(min=0, max=255), validators.Email()])
    first_name = TextField('First Name:', [])
    last_name = TextField('Last Name:', [])
    home_phone = TelField('Home Phone Number:', [validate_phone])
    cell_phone = TelField('Cell Phone Number:', [validate_phone])
    address_one = TextField('Address:', [validators.Length(min=0, max=255)])
    address_two = TextField('Address 2:', [validators.Length(min=0, max=255)])
    city = TextField('City:', [validators.Length(min=0, max=255)])
    zip_code = TextField('Zip Code:', [validators.Length(min=0, max=15)])
