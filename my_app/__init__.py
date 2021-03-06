from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from redis import Redis
from flask_wtf.csrf import CSRFProtect
import os
from flask_login import LoginManager



ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['WTF_CSRF_SECRET_KEY']  = 'random key for form'
app.config["FACEBOOK_OAUTH_CLIENT_ID"] = 'key from developer account'
app.config["FACEBOOK_OAUTH_CLIENT_SECRET"] = 'key from developer account'
app.config["GOOGLE_OAUTH_CLIENT_ID"] = "key from google console"
app.config["GOOGLE_OAUTH_CLIENT_SECRET"] = "key from google console"
app.config["OAUTHLIB_RELAX_TOKEN_SCOPE"] = True



csrf = CSRFProtect(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
#api = Api(app, decorators=[csrf.exempt])


app.secret_key = 'some_random_key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

from my_app.auth.views import auth
from my_app.auth.views import facebook_blueprint
from my_app.auth.views import google_blueprint

app.register_blueprint(auth)
app.register_blueprint(facebook_blueprint)
app.register_blueprint(google_blueprint)

db.create_all()
