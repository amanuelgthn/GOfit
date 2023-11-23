from website import db
from .models import User
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@login_required
@views.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template("dashboard.html", user={'name': current_user.firstName + " " + current_user.lastName})

@views.route('/dashboard/plan')
def plan():
    return render_template("plan.html", user={'user': current_user.firstName + " " + current_user.lastName})

@views.route('/dashboard/workout')
def workout():
    return render_template("workout.html", user={'user': current_user.firstName + " " + current_user.lastName})

@views.route('/dashboard/leaderboard')
def leaderboard():
    return render_template('leaderboard.html', user={'user': current_user.firstName + " " + current_user.lastName})