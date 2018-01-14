from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

''' Important Flask things go here
Initiate Flask App
Define Flask-SQLAlchemy Database
Initiate Login Manager
'''

app = Flask(__name__)
app.secret_key = 'supertopsecretkey'

if os.environ.get('FLASKSQLALCHEMYURI'):
    uri = os.environ.get('FLASKSQLALCHEMYURI')
else:
    uri = 'sqlite:///flaskapp_test.db'

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

