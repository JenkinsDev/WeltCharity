from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from listings.models import Listing, Comment
from weltcharity.models import User, ContactInfo, Address