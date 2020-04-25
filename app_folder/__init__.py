from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from . import forms
import flask_login

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

login = LoginManager(app)
login.login_view = "login"

from app_folder import models




current_user = flask_login.current_user

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Home")


@app.route("/gallery")
def gallery():
    return render_template('gallery.html', title="Gallery")

@app.route("/createEnvelope")
def register():
    return render_template('createEnvelope.html', title="Create Envelope")


@app.route("/login")
def login():
    current_form = forms.LoginForm()
    if current_form.validate_on_submit():
        flash('Login requested')
        return redirect('/home')
    return render_template('login.html', title="Login Page", form=current_form)
