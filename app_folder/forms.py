from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, FileField, SelectField, TextAreaField, TextField
from wtforms.validators import DataRequired

from app_folder import app
from app_folder.models import User


class LoginForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


    def check_password(self, username, password):
            user = User.query.filter_by(username=username).first()
            if user.password_hash == password:
                return True
            else:
                return False

class RegistrationForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    famchoice = SelectField('Family ',choices=[('Blue', 'Blue Ox'),('Red', 'Red Dragon'),('Yellow', 'Yellow Monkey'), ('Green', 'Green Snake')])
    password = PasswordField('Password', validators=[DataRequired()])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            flash("Username is taken.")
            raise ValidationError('Please use a different username.')


class SendMessageForm(FlaskForm):
    userMessage = TextAreaField('What is your message:', validators=[DataRequired()])
    userFrom = StringField('Who is it by', validators=[DataRequired()])
    submit = SubmitField(' Send Message ')
    
