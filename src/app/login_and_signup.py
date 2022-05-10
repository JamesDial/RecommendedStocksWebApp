from flask import request, redirect, url_for, render_template, flash, session, g
from flask_login import current_user, login_user, logout_user

import app.ufi_database as database
import re


def login():
    # Calls to the route /login will be processed here.
    logout_user()
    if current_user.is_authenticated:
        return redirect(url_for('welcome_page'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Call the database component, which handles looking up the username and password
        try:
            # Check if email/password exists
            user = database.checkForInvestor(email, password)

            # Can't let empty email and password be validated to login so must specify user length must be > 0
            # AND user must exist
            if user:
                login_user(user)
                flash(f"Login of user {email} successful!")
                return redirect(url_for('dashboard'))

        except:
            # Show message to let user know they tried to log in with invalid login
            flash(f"Invalid Email and Password combination, try logging in again or sign up.")
            return redirect(url_for('login'))

    # Default behavior is to return the login page.
    return render_template('user_login.html')


def logout():
    logout_user()
    flash(f"You have successfully logged out.")
    return redirect(url_for('welcome_page'))


def register():
    if request.method == 'GET':
        return render_template("user_signup.html")

    if request.method == 'POST' and 'password' in request.form and 'email' in request.form and 'fname' in request.form \
            and 'lname' in request.form:

        firstname = request.form['fname']
        lastname = request.form['lname']
        password = request.form['password']
        email = request.form['email']

        exists = database.checkForInvestor(email, password)

        if exists:
            flash(f'Account already exists !')
            return redirect(url_for('register'))

        else:
            if not password or not email or not firstname or not lastname:
                flash(f'Please fill out the form !')
                return redirect(url_for('register'))

            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                flash(f'Invalid email address !')
                return redirect(url_for('register'))

            elif not firstname.isalpha():
                flash(f'First name must contain only characters!')
                return redirect(url_for('register'))

            elif not lastname.isalpha():
                flash(f'Last name must contain only characters!')
                return redirect(url_for('register'))

            elif len(password) < 8:
                flash(f'Not valid password!')
                return redirect(url_for('register'))

            elif len(password) >= 13:
                flash(f'Not valid password!')
                return redirect(url_for('register'))

            elif len(password) >= 8 or len(password) < 13:
                lower = 0
                upper = 0
                digit = 0
                special = 0

                for i in password:
                    if i.islower():
                        lower += 1

                    if i.isupper():
                        upper += 1

                    if i.isdigit():
                        digit += 1

                    if not i.isnumeric() and not i.isdigit() and not i.isalpha():
                        special += 1

                if lower == 0 or upper == 0 or digit == 0 or special == 0:
                    flash(f'Not valid password!')
                    return redirect(url_for('register'))

                else:
                    database.addNewInvestor(firstname, lastname, email, password)
                    user = database.checkForInvestor(email, password)
                    login_user(user)

                    return render_template('dashboard.html')
