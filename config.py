import os

from sqlalchemy_utils import database_exists

class Config(object):
    DEBUG = True
    SECRET_HERE = 'asdfghjkl12345678'
    if os.path.exists('./config.py'):
        print('File is found')
    else:
        print('file not found')
    if database_exists('sqlite:///./db.sqlite3'):
        print('DB FOUND')
    else:
        print('NO DB')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}
    STRICT_SLASHES = False
