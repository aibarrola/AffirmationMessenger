from app_folder import app, db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    # image_file = db.Column(db.String(20), nullable = True, default ='default.jpg')
    # fam = db.Column(db.String(64), nullable=False)
    password_hash = db.Column(db.String(128))
    messages = db.relationship("Message", uselist=False, backref="user")

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userMessage = db.Column(db.String(128), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<User {}>'.format(self.username)
