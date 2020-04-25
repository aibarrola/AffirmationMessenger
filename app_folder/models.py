from app_folder import db, login
from flask_login import UserMixin

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    image_file = db.Column(db.String(20), nullable =False, default ='default.jpg')
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}'.format(self.username)