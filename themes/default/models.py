__author__ = 'bogdan'


from app import db


class DummyModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dummy_text = db.Column(db.String(64), index=True, unique=True)