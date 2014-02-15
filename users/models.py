from flask import session
from mongoengine.errors import DoesNotExist, NotUniqueError
from weltcharity import db, bcrypt
from weltcharity.settings import ROLES

import datetime


class User(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    first_name = db.StringField(max_length=35, required=False)
    last_name = db.StringField(max_length=35, required=False)
    username = db.StringField(max_length=35, required=True, unique=True)
    email = db.EmailField(max_length=255, required=True, unique=True)
    password = db.StringField(max_length=255, required=True)
    contact = db.ListField(db.EmbeddedDocumentField('ContactInfo'))
    roles = db.ListField(db.StringField(max_length=255, required=False))

    def set_users_logged_in_status(self):
        '''Handles setting up our session data that will show that the user
        has successfully become logged in.
        '''
        session.update({ 'id': str(self.id), 'logged_in': True })

    def encrypt_password(self, rounds=10):
        '''Simply uses the bcrypt library that was initialized in the __init__.py file
        of this flask project.  This method should be called before running the save
        command on the User object.

        :param rounds: The total amount of rounds to use when using the bcrypt password encryption
        '''
        self.password = bcrypt.generate_password_hash(self.password, rounds)
        return self

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
        return True

    @classmethod
    def is_username_taken(cls, username):
        '''Simple classmethod to see if we can grab a user by the
        username provided.  If we can then we know the username is
        already taken.

        :param username: User's provided username.
        '''
        try:
            cls.objects.get(username=username)
        except DoesNotExist:
            return False
        else:
            return True

    @classmethod
    def is_email_taken(cls, email):
        '''Simple classmethod to see if we can grab a user by the
        email address provided.  If we can then we know the email
        address is already taken.

        :param email: User's provided email address.
        '''
        try:
            cls.objects.get(email=email)
        except DoesNotExist:
            return False
        else:
            return True

    def __unicode__(self):
        return self.username

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'username'],
        'ordering': ['-created_at']
    }


class ContactInfo(db.EmbeddedDocument):
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
