from flask import Flask
from flask.ext.mongoengine import MongoEngine
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
    
    def setDB(self):
        self.db  = MongoEngine(self.app)

    def register_blueprints(self):
        from listings.views import listings
        from .views import home
        self.app.register_blueprint(listings)
        self.app.register_blueprint(home)

welt_charity = WeltCharity(__name__, static_folder="../static/bower_components/", static_url_path="/static")
welt_charity.setAppConfig(MONGODB_SETTINGS=DATABASE_SETTINGS, SECRET_KEY=SEC_KEY)
welt_charity.setDB()

# ALIAS
db = welt_charity.db

welt_charity.register_blueprints()

if __name__ == '__main__':
    welt_charity.app.run()