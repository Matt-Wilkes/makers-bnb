from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators


class LoginForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired(message="Email field cannot be empty"), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(message="Password field cannot be empty")])
    submit = SubmitField('Login')


class SignupForm(FlaskForm):
    email = StringField('Email', validators=[validators.DataRequired(message="Email field cannot be empty"), validators.Email()])
    password = PasswordField('Password', validators=[validators.DataRequired(message="Password field cannot be empty")])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Signup')
