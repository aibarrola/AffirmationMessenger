from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from .__init__ import app
from .models import User

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
    # image_file = sometthiiinng
    fam = StringField(['Blue Ox', 'Red Dragon', 'Yellow Monkey', 'Green Snake'], validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
