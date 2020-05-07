from flask import Flask, render_template, redirect, flash, request, url_for
from app_folder import app, db, login
from .forms import LoginForm, RegistrationForm, SendMessageForm
from app_folder.models import User, Message
from flask_login import current_user, login_required, logout_user, login_user


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Home", User=User)

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
    if current_user.is_authenticated:
        return redirect("gallery")
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect("login")
        login_user(user)
        return redirect("gallery")
    return render_template('login.html', title='Gallery', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("home")


@app.route("/gallery")
@login_required
def gallery():
    return render_template('gallery.html', title="Gallery", Users=User)

@app.route("/user/<user>", methods=['GET', 'POST'])
@login_required
def sendMessage(user):
    ToUser = User.query.filter_by(username=user).first()
    form = SendMessageForm()
    if form.validate_on_submit():
        msg = Message(user_id=ToUser.id, userMessage=form.userMessage.data, username = ToUser.username)
        db.session.add(msg)
        db.session.commit()
        return redirect("/gallery")
    return render_template('sendMessage.html', title="Send Message", ToUser=ToUser, form=form)


@app.route("/inbox", methods=['GET', 'POST'])
@login_required
def inbox():
    if not current_user.is_authenticated:
        return redirect("/home")
    user = current_user
    messages = Message.query.filter_by(username=user.username).all()
    return render_template('inbox.html', title="Inbox", user = user, messages = messages)
