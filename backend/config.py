import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://myuser:mypassword@localhost/property_violations_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
