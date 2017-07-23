import os
import pdb


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    STATIC_URL_PATH = "/static"
    STATIC_FOLDER = "lib/static"
    TEMPLATE_FOLDER = "lib/templates"


class ProductionConfig(BaseConfig):
    DEBUG = False


class StagingConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'dev.db')


class TestingConfig(BaseConfig):
    TESTING = True
