__author__ = 'bogdan'


from migrate.versioning import api
from conf import SQLALCHEMY_DATABASE_URI
from conf import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path
import logging

db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    logging.info("Creating migration folder: '%s'" %
                 SQLALCHEMY_MIGRATE_REPO)

    api.create(SQLALCHEMY_MIGRATE_REPO,
               'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI,
                        SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI,
                        SQLALCHEMY_MIGRATE_REPO,
                        api.version(SQLALCHEMY_MIGRATE_REPO))