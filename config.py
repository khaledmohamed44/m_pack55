import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///plastic_world.db')
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max-limit
    DEBUG = False
    PREFERRED_URL_SCHEME = 'https'

    # إعدادات افتراضية للموقع
    DEFAULT_SETTINGS = {
        'phone1': '+96556502009',
        'phone2': '+96550781493',
        'whatsapp': '+96556502009',
        'address': 'الشويخ الصناعية/شارع التمور/شارع 79',
        'location_url': 'https://maps.app.goo.gl/188HQpp'
    }
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 5,
        'max_overflow': 2,
        'pool_timeout': 30,
        'pool_recycle': 1800,
    }
    PROPAGATE_EXCEPTIONS = True
