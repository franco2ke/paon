import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    """shared configurations"""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    """development configrations"""
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    CONSUMER_KEY = os.getenv('CONSUMER_KEY')
    CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')

class TestingConfig(Config):
    """Configurations for Testing, with its own database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql:///test_db"
    DEBUG = True


class ProductionConfig(Config):
    """production configurations."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
