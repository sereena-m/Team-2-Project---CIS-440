import secrets
import os

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI',
        'mysql+pymysql://cis440fall24team2:cis440fall24team2@107.180.1.16:3306/cis440fall24team2'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for encryption (sessions, JWTs, etc.)
    SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_hex(32))

    # Debug mode
    DEBUG = os.getenv('FLASK_DEBUG', False)

    # SQLAlchemy engine options to handle connection pooling
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 28000,  # Recycles idle connections before timeout
        'pool_pre_ping': True   # Ensures connection validity before use
    }
