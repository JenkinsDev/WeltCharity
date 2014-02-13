import datetime
from flask import url_for
from weltcharity import db

class Listing(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    body = db.StringField(required=True)
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))

    def get_absolute_url(self):
        '''Generates a url for the listings.details URL rule. The `listings.details`
        url rule accepts one parameters which is the id of the Listing.
        '''
        return url_for('listings.details', id=self.get_id())

    def get_id(self):
        '''When you retrieve the id from a mongo document it is wrapped in class 
        instantiation like syntax.  To get rid of this we use this method to grab
        the id in it's string form.
        '''
        return str(self.id)

    def format_created_at(self, time=None):
        '''Formats the listing's created at time in a Month/Day/Year format.

        :param time: Timestmap that needs to be formated.
        '''
        if time is None:
            return self.created_at.strftime('%m/%d/%Y')
        return time.strftime('%m/%d/%Y')

    @classmethod
    def get_featured_listings(cls, limit=5, orderby="-comments"):
        '''Simple helper method for grabbing "featured" listings.  By default
        a featured listing is that which has the most comments.  This is easily
        changed by replacing the orderby parameter.

        :param limit: The amount of listings to return.
        :param orderby: The listing's field that should be used to order "featured" listings.
        '''
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
    
    def __unicode__(self):
        return self.body
