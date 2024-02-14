import os
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'database.db')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-will-never-guess'
    MAIL_SERVER = 'sandbox.smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '2b360cabc96e11'
    MAIL_PASSWORD = 'c69d6d89d96932'
    ADMINS = ['8cd85080a4-c61699+1@inbox.mailtrap.io']
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False