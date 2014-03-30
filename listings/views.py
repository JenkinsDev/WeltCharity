from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from .models import Listing, Comment


listings = Blueprint('listings', __name__, template_folder='../templates/listings')


class LatestView(MethodView):
    def get(self):
        listings = Listing.objects.all()
        return render_template('latest.html', listings=listings)


class DetailView(MethodView):
    def get(self, id):
        listing = Listing.objects.get_or_404(id=id)
        return render_template('detail.html', listing=listing)

# Register the urls
listings.add_url_rule('/listings/latest/', view_func=LatestView.as_view('latest'))
listings.add_url_rule('/listing/<id>/', view_func=DetailView.as_view('details'))
