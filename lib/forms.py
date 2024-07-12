from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, SelectField, StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, EqualTo, Length, NumberRange

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login', render_kw={'class':'btn btn-secondary'})

class SignupForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm = PasswordField('Repeat Password', validators=[InputRequired(), EqualTo('password', message="Passwords don't match")])
    submit = SubmitField('Signup', render_kw={'class':'btn btn-secondary'})

class StatusForm(FlaskForm):
    status = SelectField('Status', choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('rejected', 'Rejected')])
    submit = SubmitField('Update Status')

class NewSpaceForm(FlaskForm):
    description = TextAreaField('Description', validators=[InputRequired(), Length(1, 60, message='Description must be in 1-60 characters range')])
    name = StringField('Name', validators=[InputRequired(), Length(1, 60, message='Name must be in 1-60 characters range')])
    bedrooms = IntegerField('Bedrooms', validators=[InputRequired(),  NumberRange(0,100)])
    price = IntegerField('Price', validators=[InputRequired(), NumberRange(0, 1000000)])
    country = StringField('Country', validators=[InputRequired(), Length(1, 60, message='Country must be in 1-60 characters range')])
    city = StringField('City', validators=[InputRequired(), Length(1, 60, message='City must be in 1-60 characters range')])
    submit = SubmitField('Submit', render_kw={'class':'btn btn-secondary'})