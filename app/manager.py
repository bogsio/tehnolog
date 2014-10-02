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
    def posts(cls, page=1, rpp=10):
        return Post.query.order_by(Post.created.desc()).paginate(page, rpp, False).items

    @classmethod
    def post(cls, post_id):
        return Post.query.get(post_id)