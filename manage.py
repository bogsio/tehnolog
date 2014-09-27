import importlib
from flask.ext.script import Manager, Server, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from app import app, db, models

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("runserver", Server())
manager.add_command("shell", Shell())
manager.add_command('db', MigrateCommand)

@manager.command
def setup():
    print '[*] Setting up admin user ...'
    nickname = raw_input('[*] Nickname: ')
    email = raw_input('[*] Email: ')
    password = raw_input('[*] Password: ')
    is_valid, message = models.User.validate_password(password)
    if not is_valid:
        print '[!] ', message
        print '[!] Aborting ...'
    repeat_password = raw_input('[*] Repeat Password: ')

    if password != repeat_password:
        print '[!] Passwords do not match'
        print '[!] Aborting ...'

    user = models.User(nickname=nickname,
                       email=email)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    print '[*] Setup complete'


if __name__ == '__main__':
    manager.run()