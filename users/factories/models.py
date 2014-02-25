from flask import flash
from mongoengine.errors import DoesNotExist, NotUniqueError
from weltcharity import bcrypt
from ..models import User, ContactInfo, Address


class UserFactory():
    """UserFactory handles multiple methods of creating a user or
    logging a user in.
    """

    @staticmethod
    def get_user_info_by_id(id):
        '''Simple method that attempts to sign the user in via their
        string representation of their id.

        :param id: User's id.
        '''
        # Here we set the user to None as we will be returning the user
        # at the end. This will help stop the raising of certain exceptions.
        user = None
        try:
            user = User.objects.get(id=id)
        except DoesNotExist:
            flash("Error: Failed to access your user information, please logout and try again. Sorry for the inconvenience.", category="warning")
        return user

    @staticmethod
    def log_user_in(username_or_email, password):
        '''Attempts to log the user in by their email first and if
        it fails will revert to the username.

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
        '''Attempts to register the user, if the user has submitted
        a unique username and email address.  By the time we get to this
        point we have already validated our form data.

        :param username: User's submitted username
        :param email: User's submitted email address
        :param password: User's submitted password
        '''
        try:
            user = User(username=username, email=email, password=password).encrypt_password()
            # Here we will set up the defaults for contact_info and address. This makes settings
            # changes a lot easier.
            user.contact_info = [ContactInfo()]
            user.contact_info[0].address = [Address()]
            user.save()
        except NotUniqueError:
            if User.is_username_taken(username=username):
                flash("The username that you provided has already been taken.", category="danger")
            if User.is_email_taken(email=email):
                flash("The email address that you provided has already been taken.", category="danger")
            return False
        else:
            return user
