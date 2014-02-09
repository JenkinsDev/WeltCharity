import datetime
from . import db

class User(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    username = db.StringField(max_length=20, required=True)
    password = db.StringField(max_length=255, required=True)
    contact = db.ListField(db.EmbeddedDocumentField('ContactInfo'))

    def __unicode__(self):
        return self.username

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'username'],
        'ordering': ['-created_at']
    }


class ContactInfo(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    email = db.EmailField(max_length=255, required=True)
    phone = db.StringField(max_length=20, required=False)
    # We will be using a List field that contains EmbeddedDocumentField(s) as the user
    # we be allowed to have more than a single address.
    address = db.ListField(db.EmbeddedDocumentField('Address'))

    def __unicode__(self):
        return self.email

    meta = {
        'allow_inheritance': True,
        'indexes': ['email', 'phone']
    }


class Address(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    address_one = db.StringField(max_length=255, required=False)
    address_two = db.StringField(max_length=255, required=False)
    city = db.StringField(max_length=255, required=False)
    zip_code = db.StringField(max_length=15, required=False)

    def __unicode__(self):
        return "%s, %s" % (self.city, self.zip_code)

    meta = { 'allow_inheritance': True }