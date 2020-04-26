from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, FileField
from wtforms.validators import DataRequired

from .__init__ import app
from .models import User

famArray = [('Blue Ox', 'Blue Ox'), ('Red Dragon','Red Dragon'),
            ('Yellow Monkey','Yellow Monkey'), ('Green Snake','Green Snake')]

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


    def check_password(self, username, password):
            user = User.query.filter_by(username=username).first()
            if user.password_hash == password:
                return True
            else:
                return False

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image_file = FileField('Picture')
    fams = RadioField('Family', choices=famArray) #returns a string
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
