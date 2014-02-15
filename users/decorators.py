from flask import session, flash, redirect, url_for
from mongoengine.errors import DoesNotExist
from functools import wraps
from .models import User


def requires_user_logged_in(fn):
    """This decorator simply requires that the user
    is logged in before continue to the view.  If the
    user is not logged in we simply redirect them to the
    login page.
    """
    @wraps(fn)
    def inner(*args, **kwargs):
        if session.get('logged_in') and session.get('id'):
            try:
                user = User.objects.get(id=session.get('id'))
            except DoesNotExist:
                return redirect(url_for('home.login'))
            else:
                return fn(*args, **kwargs)
        return redirect(url_for('home.login'))
    return inner

def requires_user_not_logged_in(fn):
    """This decorator is the exact opposite of the above decorator,
    this requires that the user is not logged in.
    """
    @wraps(fn)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return fn(*args, **kwargs)
        return redirect(url_for('home.home'))
    return inner

def requires_role(fn, role):
    @wraps(fn)
    def inner(*args, **kwargs):
        user = User.objects.get(id=session.get('id'))
        if not user.has_role(role=role):
            flash("You do not have the required permissions to access this area.", category="error")
            return redirect(url_for('home.home'))
        return fn(*args, **kwargs)
    return inner
