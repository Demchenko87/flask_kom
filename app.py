from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import SQLAlchemyUserDatastore, Security


app = Flask(__name__, static_folder='static')
app.config.from_object(Configuration)


db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import *
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


