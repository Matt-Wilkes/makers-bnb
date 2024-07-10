from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired, EqualTo


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


class SignupForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm = PasswordField('Repeat Password', validators=[InputRequired(), EqualTo('password', message="Passwords don't match")])
    submit = SubmitField('Signup')

class StatusForm(FlaskForm):
    status = SelectField('Status', choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('rejected', 'Rejected')])
    submit = SubmitField('Update Status')
