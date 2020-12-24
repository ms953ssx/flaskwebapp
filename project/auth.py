from flask_login import login_user, logout_user, login_required
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    customer_email = request.form.get('email')
    customer_password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(customer_email=customer_email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.customer_password, customer_password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) #if the user doesnt exist or password is wrong, reload the page
    # if the above check passes, then we know the user has the correct credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/passreset')
def passreset():
    return render_template('passreset.html')

def passreset_post():
    #code for reset password will go here
    customer_email = request.form.get('email')
    customer_confirm_email = request.form.get('confirm_email')

    user = User.query.filter_by(customer_email=customer_email).first() # check if account exists with email

    if customer_email != customer_confirm_email:
        flash('Emails do not match! Please try again.')
        return redirect(url_for('auth.passreset')) #if both email addresses do not match, reload the page
    
    #if above check passes, check if email exists in database
    user = User.query.filter_by(customer_email=customer_email).first() # check if account exists with email
    
    if not user:
        flash('Email address does not exist!')
        return redirect(url_for('auth.passreset'))
    
    # code for sending password reset will go here


    return redirect(url_for('main.index'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    customer_email = request.form.get('email')
    customer_name = request.form.get('name')
    customer_password = request.form.get('password')

    user = User.query.filter_by(customer_email=customer_email).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data.. Hash the password so the plaintext version isnt saved
    new_user = User(customer_email=customer_email, customer_name=customer_name, customer_password=generate_password_hash(customer_password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
