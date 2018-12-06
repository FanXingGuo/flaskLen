from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from fscript import app

from day02.exts import db

manager=Manager(app)
Migrate(app,db)
manager.add_command("db",MigrateCommand)

if __name__ == '__main__':
    manager.run()