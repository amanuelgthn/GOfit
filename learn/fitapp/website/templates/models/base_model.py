#!/usr/bin/python3
"""
Base model for the fitapp containing basic information of the user
"""

from datetime import datetime
from os import getenv
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base()

class BaseModel:
    id= Column(String(60), primary_key=True, nullable=False)
    created_at= Column(DateTime, default=datetime.utcnow)
    updated_at= Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name, self.id, self.__dict__)
