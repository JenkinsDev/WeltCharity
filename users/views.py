from flask import Blueprint, flash, request, redirect, render_template, session, url_for
from flask.views import MethodView, View
from mongoengine.errors import NotUniqueError, DoesNotExist
from weltcharity import bcrypt
from listings.models import Listing, Comment
from .models import User, ContactInfo
from .forms import RegistrationForm, LoginForm
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
        if request.method == 'POST' and self.form.validate():
            user = UserFactory.log_user_in(
                    self.form.username_or_email.data,
                    self.form.password.data
                )
            if user:
                user.set_users_logged_in_status()
                return redirect(url_for('home.home'))
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
        if request.method == 'POST' and self.form.validate():
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
        if session.get('id'):
            del session['id']
        if session.get('logged_in'):
            del session['logged_in']
        flash("You have successfully been logged out!", category="success")
        return redirect(url_for('users.login'))


users.add_url_rule('/login/', view_func=LoginView.as_view('login'))
users.add_url_rule('/register/', view_func=RegisterView.as_view('register'))
users.add_url_rule('/log-out/', view_func=LogoutView.as_view('logout'))
