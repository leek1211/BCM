import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
ADMINS = frozenset('1211leek@gmail.com')
SECRET_KEY = 'This string will be replaced with a proper key in production.'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

WTF_CSRF_ENABLED = False 