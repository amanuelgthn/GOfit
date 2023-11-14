#!/usr/bin/python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    """ app.config['SECRET_KEY'] = 'secret_key_gofit'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(DB_NAME)
    db.init_app(app) """

    # Static file congfiguration
    app.static_folder = 'static'
    app.static_url_path = '/static'

    from .templates.views import views
    from .templates.auth import auth


    #Blueprint registration
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')



    return app