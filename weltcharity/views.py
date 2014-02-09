from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from .models import User, ContactInfo
from listings.models import Listing, Comment

home = Blueprint('home', __name__, template_folder='../templates')


class HomeView(MethodView):
    def get(self):
        listings = Listing.objects.all()
        return render_template('home.html', listings=listings)


# Register the urls
home.add_url_rule('/', view_func=HomeView.as_view('home'))