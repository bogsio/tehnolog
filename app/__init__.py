__author__ = 'bogdan'


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import jinja2
import conf
import os
import logging

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['BASE_DIR'] = conf.BASE_DIR
app.config['SQLALCHEMY_DATABASE_URI'] = conf.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_MIGRATE_REPO'] = conf.SQLALCHEMY_MIGRATE_REPO
app.config['THEME'] = conf.THEME


theme_loader = jinja2.ChoiceLoader([
        app.jinja_loader,
        jinja2.FileSystemLoader([
            os.path.join(conf.BASE_DIR, 'themes'),
        ]),
    ])

app.jinja_loader = theme_loader

from app import views, models

logging.info('[+] Loaded configuration ...')