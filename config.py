from os import path


class Config(object):
    DEBUG = False


class Development(Config):
    DEBUG = True
    SECRET_KEY = 'development'
    PORT = 5000
    HOST = '0.0.0.0'
    URL_PREFIX = '/api'
    PROJECT_ROOT = path.abspath(path.dirname(__file__))
    TEMPLATE_FOLDER = path.join(PROJECT_ROOT, 'templates')
    SQLALCHEMY_DATABASE_URI = 'sqlite:////meetneat.db'
    LOGGING_FORMAT = '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
