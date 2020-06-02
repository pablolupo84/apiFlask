class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG =True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost/api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development':DevelopmentConfig
}