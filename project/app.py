#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Built-in/Generic Imports
import os

# Libs
from flask import Flask, render_template, g, request

# Own modules
from .extensions import db, babel, manager, migrate
from .frontend import frontend
from .api import initialize_api

__all__ = ("create_app")

BLUEPRINTS = [frontend]


def create_app(config=None, app_name="project", blueprints=None):
    """Create the application."""
    app = Flask(
        app_name,
        static_folder=os.path.join(os.path.dirname(__file__), "static"),
        template_folder="templates",
    )

    app.config.from_object("project.config")
    app.config.from_pyfile("../local.cfg", silent=True)
    if config:
        app.config.from_pyfile(config)

    if blueprints is None:
        blueprints = BLUEPRINTS

    blueprints_fabrics(app, blueprints)
    extensions_fabrics(app)
    api_fabrics(app)
    configure_logging(app)

    gvars(app)

    return app


def blueprints_fabrics(app, blueprints):
    """Configure blueprints."""
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def extensions_fabrics(app):
    """Configure extensions."""
    db.init_app(app)
    babel.init_app(app)
    migrate.init_app(app, db)


def api_fabrics(app):
    """Configure API."""
    initialize_api(app)
    manager.init_app(app)


def gvars(app):
    @app.before_request
    def guser():
        g.user = 'fakeUser'

    @app.context_processor
    def inject_user():
        try:
            return {"user": g.user}
        except AttributeError:
            return {"user": None}
    
    @app.context_processor
    def active_blueprint():
        return {request.blueprint: True}
    
    @babel.localeselector
    def get_locale():
        accept_languages = app.config.get("ACCEPT_LANGUAGES")
        return request.accept_languages.best_match(accept_languages)


def configure_logging(app):
    """Configure file(info) logging."""
    if app.debug or app.testing:
        # Skip debug and test mode. Just check standard output.
        return

    import logging
    import logging.handlers

    # Set info level on logger, which might be overwritten by handers.
    # Suppress DEBUG messages.
    app.logger.setLevel(logging.INFO)

    info_log = os.path.join(app.config["LOG_FOLDER"], "info.log")
    info_file_handler = logging.handlers.RotatingFileHandler(
        info_log, maxBytes=100000, backupCount=10
    )
    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s: %(message)s " "[in %(pathname)s:%(lineno)d]"
        )
    )
    app.logger.addHandler(info_file_handler)
