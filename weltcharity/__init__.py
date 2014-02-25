from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.bcrypt import Bcrypt
from flask_wtf.csrf import CsrfProtect
from .settings import DATABASE_SETTINGS, SEC_KEY


class WeltCharity:
    """ WeltCharity will be used a simple wrapper class that will
    help instantiate our Flask instance along with setup our database
    connections.
    """
    def __init__(self, name, static_folder, static_url_path):
        self.app = Flask(name, static_folder=static_folder, static_url_path=static_url_path)

    def setAppConfig(self, **kwargs):
        for key, value in kwargs.items():
            self.app.config[key] = value
    
    def setDB(self, app=None):
        if not app:
            self.db = MongoEngine(self.app)
        else:
            self.db = MongoEngine(app)

    def setBcrypt(self, app=None):
        if not app:
            self.bcrypt = Bcrypt(self.app)
        else:
            self.bcrypt = Bcrypt(app)

    def enableCSRFProtection(self, app=None):
        if not app:
            self.csrf = CsrfProtect(self.app)
        else:
            self.csrf = CsrfProtect(app)

    def register_blueprints(self):
        '''Handles the registration of all of our blueprints in a
        manual fashion. Imports are added inside of this method so
        we don't have to worry about circular imports.
        '''
        from listings.views import listings
        from .views import base
        from admin.views import admin
        from users.views import users
        self.app.register_blueprint(listings)
        self.app.register_blueprint(base)
        self.app.register_blueprint(admin)
        self.app.register_blueprint(users)


welt_charity = WeltCharity(__name__, static_folder="../static/", static_url_path="/static")
welt_charity.setAppConfig(MONGODB_SETTINGS=DATABASE_SETTINGS, SECRET_KEY=SEC_KEY)
welt_charity.setDB()
welt_charity.setBcrypt()
welt_charity.enableCSRFProtection()

# ALIAS
db = welt_charity.db
bcrypt = welt_charity.bcrypt

welt_charity.register_blueprints()

if __name__ == '__main__':
    welt_charity.app.run()