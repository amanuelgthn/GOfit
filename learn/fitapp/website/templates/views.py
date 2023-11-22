from website import db
from .models import User
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html", user=current_user)

@login_required
@views.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", user=current_user)

@views.route('/dashboard/plan')
def plan():
    return render_template("plan.html")

@views.route('/dashboard/workout')
def workout():
    return render_template("workout.html")