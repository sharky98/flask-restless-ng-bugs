#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Built-in/Generic Imports

# Libs
from flask_script import Manager
from flask_migrate import MigrateCommand

# Own modules
from project import create_app
from project.extensions import db

manager = Manager(create_app)

# Add Flask-Migrate commands under `db` prefix, for example:
# $ python manage.py db init
# $ python manage.py db migrate
manager.add_command('db', MigrateCommand)


@manager.command
def init():
    """Run in local machine."""
    syncdb()


@manager.command
def syncdb():
    """Init/reset database."""
    db.drop_all()
    db.create_all()

if __name__ == "__main__":
    manager.run()
