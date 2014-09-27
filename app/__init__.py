__author__ = 'bogdan'


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from app import views

app = Flask(__name__)
db = SQLAlchemy(app)

