from flask import flash
from mongoengine.errors import DoesNotExist, NotUniqueError
from weltcharity import bcrypt
from ..models import User, ContactInfo, Address


class UserFactory():
    """UserFactory handles multiple methods of creating a user or
    logging a user in.
    """

    @staticmethod
    def log_user_in(username_or_email, password):
        '''Attempts to log the user in by their email first and if
        it fails will revert to the username.  If the user does log
        in then we 

        :param username_or_email: User's submitted username or email.
        :param password: User's submitted password.
        '''
        try:
            user = User.objects.get(email=username_or_email)
        except DoesNotExist:
            try:
                user = User.objects.get(username=username_or_email)
            except DoesNotExist:
                return False
        if bcrypt.check_password_hash(user.password, password):
            return user

    @staticmethod
    def register_user(username, email, password):
        try:
            user = User(username=username, email=email, password=password).encrypt_password().save()
        except NotUniqueError:
            if User.is_username_taken(username=username):
                flash("The username that you provided has already been taken.", category="error")
            if User.is_email_taken(email=email):
                flash("The email address that you provided has already been taken.", category="error")
        else:
            return user
