from flask.ext.script import Manager, Server, Shell
from flask.ext.migrate dimport Migrate, MigrateCommand
from app import app, db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("runserver", Server())
manager.add_command("shell", Shell())
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()