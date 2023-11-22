#!/usr/bin/python3
from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    workouts = db.relationship('Workout')

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    workout_name = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
