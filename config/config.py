
class Config:
    SECRET_KEY = '$2b$12$0//Ohjx84OhQvSD5V6qw8u5gPRNBgjZBVoPiPtikSgbejd3'

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True





