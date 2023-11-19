#!/usr/bin/python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = 'fit_db'
DB_USER = 'fit_usr' 
DB_PASS = 'fit_usr_pwd'
DB_HOST = 'localhost'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key_gofit'
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{}:{}@{}/{}".format(DB_USER, DB_PASS, DB_HOST, DB_NAME)
    db.init_app(app)

    # Static file congfiguration
    app.static_folder = 'static'
    app.static_url_path = '/static'

    from .templates.views import views
    from .templates.auth import auth


    #Blueprint registration
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .templates.models import User
    create_database(app)

    return app

def create_database(app):
    with app.app_context():
        db.create_all()
    print("Database created successfully!")