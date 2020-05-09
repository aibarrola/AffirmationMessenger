import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = 'you-will-never-guess'

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    # SQLALCHEMY_DATABASE_URI = 'DATABASE_URL'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

