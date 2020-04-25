from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)

login = LoginManager(app)
login.login_view = "login"

from app_folder import models 



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
    current_form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested')
        return redirect('/home')
    return render_template('login.html', title="Login Page", form=current_form)

if __name__ == "__main__":
    app.run(debug=True)

