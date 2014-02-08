import datetime
from flask import url_for
from weltcharity import welt_charity


class Listing(welt_charity.db.Document):
    created_at = welt_charity.db.DateTimeField(default=datetime.datetime.now, required=True)
    title = welt_charity.db.StringField(max_length=255, required=True)
    slug = welt_charity.db.StringField(max_length=255, required=True)
    body = welt_charity.db.StringField(required=True)
    comments = welt_charity.db.ListField(welt_charity.db.EmbeddedDocumentField('Comment'))

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }


class Comment(welt_charity.db.EmbeddedDocument):
    created_at = welt_charity.db.DateTimeField(default=datetime.datetime.now, required=True)
    body = welt_charity.db.StringField(verbose_name="Comment", required=True)
    author = welt_charity.db.StringField(verbose_name="Name", max_length=255, required=True)