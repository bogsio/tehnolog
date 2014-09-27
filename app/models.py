__author__ = 'bogdan'


import datetime
import importlib
import logging
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session
from app import app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(120))
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    posts = db.relationship('Post', backref='author',
                            lazy='dynamic')

    def set_password(self, password):
        pass

    def check_password(self, password):
        pass

    @staticmethod
    def authenticate(email, password):
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            # Check if the password is correct
            correct_password = existing_user.check_password(password)
            if correct_password:
                # Login the user
                return existing_user, None
            else:
                return None, 'Wrong Password'

        else:
            return None, 'Email not registered'

    @staticmethod
    def validate_password(password):
        if len(password) >= 8:
            return True, 'Valid Password'
        return False, 'Passwords should have at least 8 characters'

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)

    def set_password(self, password):
        self.password = self.hash_password(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def login(self):
        if not self.email:
            return False
        session['USER_ID'] = self.id

        logging.info('Logged In user: %s' % self.email)
        return True

    @staticmethod
    def logout():
        del session['USER_ID']

    def __repr__(self):
        return '<User %r>' % (self.nickname)

    @staticmethod
    def get_current_user():
        try:
            user = User.query.get(int(session['USER_ID']))
            return user
        except KeyError:
            return None
        except ValueError:
            del session['USER_ID']
            return None


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), default='Title')
    content = db.Column(db.Text, default='')
    summary = db.Column(db.Text, default='')
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % self.title


importlib.import_module('themes.' + app.config['THEME'] + '.models')