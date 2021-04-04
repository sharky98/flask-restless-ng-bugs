#!/usr/bin/env python
# -*- coding: utf-8 -*-

# General Config
DEBUG = True
SECRET_KEY = '56bf4s4fd45yt364563yDFGH/%$?'
LOG_FOLDER = 'logs'

# Database Config
from os.path import dirname, abspath
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/data.sqlite' % dirname(abspath(__file__))
SQLALCHEMY_ECHO = True
del dirname, abspath

# default babel values
BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_TIMEZONE = 'UTC'
ACCEPT_LANGUAGES = ['en', 'fr', ]

# available languages
LANGUAGES = {
    'en': u'English',
    'fr': u'Français'
}
