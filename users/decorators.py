from flask import session, flash, redirect, url_for
from mongoengine.errors import DoesNotExist
from functools import update_wrapper, wraps
from .models import User


def requires_user_logged_in():
    """This decorator simply requires that the user
    is logged in before continue to the view.  If the
    user is not logged in we simply redirect them to the
    login page.
    """
    def decorator(fn):
        def inner(*args, **kwargs):
            if session.get('logged_in') and session.get('ident'):
                try:
                    user = User.objects.get(id=session.get('ident'))
                except DoesNotExist:
                    return redirect(url_for('users.login'))
                else:
                    return fn(*args, **kwargs)
            return redirect(url_for('users.login'))
        return update_wrapper(inner, fn)
    return decorator

def requires_user_not_logged_in():
    """This decorator is the exact opposite of the above decorator,
    this requires that the user is not logged in.
    """
    def decorator(fn):
        def inner(*args, **kwargs):
            if not session.get('logged_in'):
                return fn(*args, **kwargs)
            return redirect(url_for('home.home'))
        return update_wrapper(inner, fn)
    return decorator

def requires_role(role=None):
    """Simple decorator that requires the user to have the specified role
    to be able to access the view.  If you are going to call this decorator
    you must ALWAYS call the requires_user_logged_in decorator first so you
    know the user is definitely logged in.
    """
    def decorator(f):
        def inner(*args, **kwargs):
            user = User.objects.get(id=session.get('ident'))
            if not user.has_role(role=role):
                flash("You do not have the required permissions to access this area.", category="error")
                return redirect(url_for('home.home'))
            return fn(*args, **kwargs)
        return update_wrapper(inner, f)
    return decorator
