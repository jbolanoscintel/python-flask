class BaseConfig:
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    TESTING = True

class ProductionConfig(BaseConfig):
    pass