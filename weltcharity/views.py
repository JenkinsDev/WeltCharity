from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from .models import Listing, Comment

listings = Blueprint('listings', __name__, template_folder='templates')


class ListView(MethodView):
    def get(self):
        listings = Listing.objects.all()
        return render_template('listings/home.html', listings=listings)


class DetailView(MethodView):
    def get(self, slug):
        listing = Listing.objects.get_or_404(slug=slug)
        return render_template('listings/detail.html', listing=listing)


# Register the urls
listings.add_url_rule('/', view_func=ListView.as_view('home'))
listings.add_url_rule('/<slug>/', view_func=DetailView.as_view('detail'))