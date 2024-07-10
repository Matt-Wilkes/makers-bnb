# This file is to handle all the routes for the user - login, signup, home, logout, view-space
import os

from flask import Flask, render_template, redirect, url_for, flash, request, session

from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User
from lib.forms import LoginForm, SignupForm


def user_routes(app):
    @app.route('/')
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                user = UserRepository(get_flask_database_connection(app)).find(form.email.data, form.password.data)
                if user:
                    # print(user.__dict__)
                    session['active'] = True
                    session['id'] = user.id
                    session['email'] = user.email
                    return redirect('/home')
                else:
                    flash('Wrong email/password combination')
                    render_template('login.html', form=form)
        return render_template('login.html', form=form)

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        form = SignupForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                user = UserRepository(get_flask_database_connection(app)).create(User(None, form.email.data, form.password.data))
                if user:
                    # print(user.items())
                    session['active'] = True
                    session['id'] = user['id']
                    session['email'] = user['email']
                    return redirect('/home')
                else:
                    flash('User with such email already exists')
                    render_template('signup.html', form=form)
        return render_template('signup.html', form=form)


    @app.route('/logout')
    def logout():
        session.pop('active', None)
        session.pop('id', None)
        session.pop('email', None)
        return redirect(url_for('login'))

    if __name__ == '__main__':
        app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
