#!/usr/bin/python3
"""
Database storage
"""

from ..base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class DBStorage:
    __engine = None
    __session = None


    DB_NAME = 'fit_db'
    DB_USER = 'fit_usr'
    DB_PASS = 'fit_usr_pwd'
    DB_HOST = 'localhost'

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                    format(self.DB_USER,
                           self.DB_PASS,
                           self.DB_HOST,
                           self.DB_NAME))
    
    def new(self, obj):
        self.__session.add(obj)
    
    def save(self, obj):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session