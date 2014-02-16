from flask import Blueprint, flash, request, redirect, render_template, session, url_for
from flask.views import MethodView, View
from mongoengine.errors import NotUniqueError, DoesNotExist
from weltcharity import bcrypt
from listings.models import Listing, Comment
from .models import User, ContactInfo, Address
from .forms import RegistrationForm, LoginForm, GeneralAccountSettingsForm
from .factories.models import UserFactory
from .decorators import requires_user_not_logged_in, requires_user_logged_in



users = Blueprint('users', __name__, template_folder='../templates/users')

class LoginView(View):
    """LoginView handles the GET and POST requests.  This View is considered a normal
    view over a MethodView to help cut down on the repetition of code.  Less boilerplate.
    """
    methods = ['GET', 'POST']
    decorators = [requires_user_not_logged_in()]

    def __init__(self):
        self.form = LoginForm(request.form)
    
    def dispatch_request(self):
        if request.method == 'POST' and self.form.validate_on_submit():
            user = UserFactory.log_user_in(
                    self.form.username_or_email.data,
                    self.form.password.data
                )
            if user:
                user.set_users_logged_in_status()
                return redirect(url_for('home.home'))
            # If the user from above was not signed in then we will get to here and
            # we know the user failed to login, time to let the user know they failed.
            flash("Username/Email or Password is incorrect.")
        return render_template('login.html', form=self.form)


class RegisterView(View):
    """RegisterView handles the GET and POST data when handling registration requests.
    This View is considered a normal view over a MethodView to help cut down on the
    repetition of code.
    """
    methods = ['GET', 'POST']
    decorators = [requires_user_not_logged_in()]

    def __init__(self):
        self.form = RegistrationForm(request.form)

    def dispatch_request(self):
        if request.method == 'POST' and self.form.validate_on_submit():
            user = UserFactory.register_user(
                    self.form.username.data,
                    self.form.email.data,
                    self.form.password.data
                )
            if user:
                return redirect(url_for('users.login'))
        return render_template('register.html', form=self.form)


class LogoutView(View):
    """LogoutView only allows access via a GET request and simply terminates the session
    stating the user is logged in.
    """
    decorators = [requires_user_logged_in()]

    def dispatch_request(self):
        if session.get('ident'):
            del session['ident']
        if session.get('logged_in'):
            del session['logged_in']
        flash("You have successfully been logged out!", category="success")
        return redirect(url_for('users.login'))


class SettingsView(View):
    """SettingsView handles accessing the form to view and change your user settings.
    """
    methods = ['GET', 'POST']
    decorators = [requires_user_logged_in()]

    def __init__(self):
        self.form = GeneralAccountSettingsForm(request.form)
        self.user = UserFactory.get_user_info_by_id(session.get('ident'))

    def dispatch_request(self):
        if request.method == 'POST' and self.form.validate_on_submit():
            if self.user:
                contact_info = ContactInfo(
                        home_phone=self.form.home_phone.data,
                        cell_phone=self.form.cell_phone.data
                )
                address = Address(
                        address_one=self.form.address_one.data,
                        address_two=self.form.address_two.data,
                        city=self.form.city.data,
                        zip_code=self.form.zip_code.data
                    )
                self.user = User.objects.get(id=session.get('ident'))
                # After getting out user we set the contact info and address data
                # but we need to make sure to set our data to the first element
                # in the list.  We will be adding support for multiple phones and
                # multiple addresses in the future, but for now this is our work-around.
                self.user.contact_info[0] = contact_info
                self.user.contact_info[0].address = [address]
                self.user.save()
        return render_template('settings.html', form=self.form, user=self.user)

users.add_url_rule('/login/', view_func=LoginView.as_view('login'))
users.add_url_rule('/register/', view_func=RegisterView.as_view('register'))
users.add_url_rule('/logout/', view_func=LogoutView.as_view('logout'))
users.add_url_rule('/account/settings/', view_func=SettingsView.as_view('settings'))
