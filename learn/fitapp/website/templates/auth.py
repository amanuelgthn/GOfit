#!/usr/bin/python3
from website import db
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User



auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET','POST'])
def login():
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)

        user = User.query.filter_by(email=email).first()
        if user:
            if password == user.password:
                flash("Logged in Successfully", category="success")
                login_user(user, remember=True)
                return redirect(url_for('views.dashboard'))"""
    data = request.form
    print (data)

    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        #lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email = email).first()

        if user:
            flash("Email already Exists please login", category="error")
        elif len(firstName) < 3:
            flash("First Name must be at least 3 characters", category="error")
        #elif len(lastName) < 3:
            #flash("Last Name must be at least 3 characters", category="error")
        elif password1 != password2:
            flash("Password must be the same")
        else:
            new_user = User(email=email, firstName=firstName, lastName=lastName, password=password1, password2=password2)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Successfully created {}'.format(new_user))
            return redirect(url_for('views.dashboard'))
    return render_template('register.html', user=current_user)

            


    return render_template('register.html')