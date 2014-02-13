from flask import session
from . import db, bcrypt
from .settings import ROLES

import datetime


class User(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    username = db.StringField(max_length=20, required=True)
    password = db.StringField(max_length=255, required=True)
    contact = db.ListField(db.EmbeddedDocumentField('ContactInfo'))
    roles = db.ListField(db.StringField(max_length=255, required=False))

    def log_user_in(self, username, password):
        '''Attempts to log the user in.
        
        :param username: The string representation of the user.
        :param password: The user's password or passphrase.
        '''
        user = User.objects.get(username=username)
        if bcrypt.check_password_hash(user.password, password):
            session.update({ 'id'=self.id, 'logged_in'=True })
            return True
        return False

    def encrypt_password(self, rounds=10):
        '''Simply uses the bcrypt library that was initialized in the __init__.py file
        of this flask project.  This method should be called before running the save
        command on the User object.

        :param rounds: The total amount of rounds to use when using the bcrypt password encryption
        '''
        self.password = bcrypt.generate_password_hash(self.password, rounds)

    def has_role(self, role):
        '''Checks to see if a user has the supplied role.  Returns a boolean value;
        true if the user does have the role, else false.

        :param role: String identifier for a specific role.
        '''    
        return ROLES[role] in self.roles

    def has_roles(self, roles):
        '''Wrapper around the has_role method that allows you to check if a user has all
        of the roles provided.

        :param roles: List or tuple containing the string identifiers for roles.
        '''
        for role in roles:
            if not self.has_role(role=role):
                return False

    def __unicode__(self):
        return self.username

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'username'],
        'ordering': ['-created_at']
    }


class ContactInfo(db.EmbeddedDocument):
    email = db.EmailField(max_length=255, required=True)
    phone = db.StringField(max_length=20, required=False)
    address = db.ListField(db.EmbeddedDocumentField('Address'))

    def __unicode__(self):
        return self.email

    meta = {
        'allow_inheritance': True,
        'indexes': ['email', 'phone']
    }


class Address(db.EmbeddedDocument):
    address_one = db.StringField(max_length=255, required=False)
    address_two = db.StringField(max_length=255, required=False)
    city = db.StringField(max_length=255, required=False)
    zip_code = db.StringField(max_length=15, required=False)

    def __unicode__(self):
        return "%s, %s" % (self.city, self.zip_code)

    meta = { 'allow_inheritance': True }
