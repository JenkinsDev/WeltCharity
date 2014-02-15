from flask import Blueprint, flash, render_template
from flask.views import MethodView
from listings.models import Listing, Comment

import bcrypt


base = Blueprint('home', __name__, template_folder='../templates')

class HomeView(MethodView):

    def get(self):
        listings = Listing.get_featured_listings()
        return render_template('home.html', listings=listings)


# Register the urls
base.add_url_rule('/', view_func=HomeView.as_view('home'))
