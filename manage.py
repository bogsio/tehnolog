from flask.ext.script import Manager, Server, Shell
from app import app

manager = Manager(app)
manager.add_command("runserver", Server())
manager.add_command("shell", Shell())
manager.run()