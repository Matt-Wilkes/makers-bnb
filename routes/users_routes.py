from flask import render_template, redirect, url_for, flash, request, session

from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.user_repository import UserRepository
from lib.forms import LoginForm, SignupForm

def users_routes(app):
    @app.route('/about')
    def about():
        return render_template('about.html')

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

    @app.route('/home')
    def home():
        return render_template('home.html')

    @app.route('/logout')
    def logout():
        session.pop('active', None)
        session.pop('id', None)
        session.pop('email', None)
        flash('You were logged out')
        return redirect(url_for('login'))