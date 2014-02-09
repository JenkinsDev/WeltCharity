import datetime
from flask import url_for
from weltcharity import db

class Listing(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    body = db.StringField(required=True)
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))

    def get_absolute_url(self):
        return url_for('listings.details', id=self.get_id())

    def get_id(self):
        return str(self.id)

    def format_created_at(self, time=None):
        if time is None:
            return self.created_at.strftime('%m/%d/%Y')
        return time.strftime('%m/%d/%Y')

    # We create a simple interface for grabbing the "featured" listings,
    # the reason this interface was created is because we will have easy
    # access to change what constitutes as a "featured" listing.
    @classmethod
    def get_featured_listings(cls, limit=5, orderby="-comments"):
        return cls.objects.limit(limit).order_by(orderby)

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }


class Comment(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(verbose_name="Comment", required=True)
    author = db.StringField(verbose_name="Name", max_length=255, required=True)
