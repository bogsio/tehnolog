from flask import session, request
from app import app
from app.models import User, Post


class ModelManager(object):

    @classmethod
    def current_user(cls):
        try:
            user = User.query.get(session['USER_ID'])
            return user
        except KeyError:
            return None

    @classmethod
    def posts(cls, page=1):
        return Post.query.all()

    @classmethod
    def post(cls, post_id):
        pass