from flask import Flask, render_template, redirect, flash, request, url_for
from app_folder import app, db, login
from .forms import LoginForm, RegistrationForm
from app_folder.models import User
from flask_login import current_user, login_required, logout_user, login_user


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Home", User=User)


@app.route("/gallery")
def gallery():
    return render_template('gallery.html', title="Gallery")

@app.route("/createEnvelope", methods=['GET', 'POST'])
def register():
    current_form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect (url_for('/'))
    if current_form.validate_on_submit():
        login_user = User(username=current_form.username.data)
        login_user.set_password(current_form.password.data)
        db.session.add(login_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('createEnvelope.html', title="Create Envelope", form=current_form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    current_form = LoginForm()
    if current_form.validate_on_submit():
        return redirect('/home')
    return render_template('login.html', title="Login Page", form=current_form)
