__author__ = 'bogdan'


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import conf

app = Flask(__name__)
db = SQLAlchemy(app)

from app import views, models

app.config['BASE_DIR'] = conf.BASE_DIR
app.config['SQLALCHEMY_DATABASE_URI'] = conf.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_MIGRATE_REPO'] = conf.SQLALCHEMY_MIGRATE_REPO

