#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Libs
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
import flask_restless
from flask_migrate import Migrate

db = SQLAlchemy()
babel = Babel()
manager = flask_restless.APIManager(flask_sqlalchemy_db=db)
migrate = Migrate()