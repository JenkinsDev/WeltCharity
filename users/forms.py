from flask_wtf import Form
from flask_wtf.html5 import EmailField, TelField
from wtforms import BooleanField, TextField, PasswordField, validators
from datetime import timedelta
from .models import User

import re


def validate_phone(form, field):
    """ Simple validation for checking to see if the user has
    submitted a valid Phone Number.

    :param form: Form data that the field we are validating against
                 exists within.
    :param field: Field data that we will be validating against.
    """
    result = re.match(r'1?\W*([2-9][0-8][0-9])\W*([2-9][0-9]{2})\W*([0-9]{4})(\se?x?t?(\d*))?', field.data)
    if len(field.data) > 0 and not result:
    	raise validators.ValidationError('Phone must be a valid phone number')

def validate_username_doesnt_exist(form, field):
    """ Checks against the database to see if the username submitted exists
    already or not.

    :param form: Form data that the field we are validating against
                 exists within.
    :param field: Field data that we will be validating against.
    """
    if User.is_username_taken(field.data) and not User.is_this_current_users_username(field.data):
        raise validators.ValidationError('The Username that you have provided is already taken.')

def validate_email_doesnt_exist(form, field):
    """ Checks against the database to see if the username submitted exists
    already or not.

    :param form: Form data that the field we are validating against
                 exists within.
    :param field: Field data that we will be validating against.
    """
    if User.is_email_taken(field.data) and not User.is_this_current_users_email(field.data):
        raise validators.ValidationError('The Email that you have provided is already taken.')


class RegistrationForm(Form):
    username = TextField('Username:', [validators.Length(min=5, max=35), validate_username_doesnt_exist])
    email = EmailField('Email Address:', [validators.Length(min=0, max=255), validators.Email(), validate_email_doesnt_exist])
    password = PasswordField('Password:', [validators.InputRequired(), validators.EqualTo('password_conf', message='Passwords must match')])
    password_conf = PasswordField('Password Confirmation:', [validators.InputRequired()])


class LoginForm(Form):
    username_or_email = TextField('Username or Email Address:', [validators.InputRequired()])
    password = PasswordField('Password:', [validators.InputRequired()])


class GeneralAccountSettingsForm(Form):
    username = TextField('Username:', [validators.Length(min=5, max=35), validate_username_doesnt_exist])
    email = EmailField('Email Address:', [validators.Length(min=0, max=255), validators.Email(), validate_email_doesnt_exist])
    first_name = TextField('First Name:', [])
    last_name = TextField('Last Name:', [])
    home_phone = TelField('Home Phone Number:', [validate_phone])
    cell_phone = TelField('Cell Phone Number:', [validate_phone])
    address_one = TextField('Address:', [validators.Length(min=0, max=255)])
    address_two = TextField('Address 2:', [validators.Length(min=0, max=255)])
    city = TextField('City:', [validators.Length(min=0, max=255)])
    zip_code = TextField('Zip Code:', [validators.Length(min=0, max=15)])
