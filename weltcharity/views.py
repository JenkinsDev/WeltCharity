from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from .models import User, ContactInfo
from . import bcrypt
from listings.models import Listing, Comment


base = Blueprint('home', __name__, template_folder='../templates')

class HomeView(MethodView):
    def get(self):
        listings = Listing.get_featured_listings()
        return render_template('home.html', listings=listings)


class LoginView(MethodView):
    def get(self):
        return render_template('users/login.html')

    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        return render_template('users/login.html')


class RegisterView(MethodView):
    def get(self):
        return render_template('users/register.html')

    def post(self):
        return render_template('users/register.html')


# Register the urls
base.add_url_rule('/', view_func=HomeView.as_view('home'))
base.add_url_rule('/login/', view_func=LoginView.as_view('login'))
base.add_url_rule('/register/', view_func=RegisterView.as_view('register'))