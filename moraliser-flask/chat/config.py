"""
Global Flask Application Setting

See `.flaskenv` for default settings.
 """

import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    # If not set fall back to production for safety
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    # Set FLASK_SECRET on your production Environment
    SECRET_KEY = os.getenv('FLASK_SECRET', 'Secret')

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    # DIST_DIR = os.path.join(ROOT_DIR, 'dist')
    # STATIC_DIR = os.path.join(DIST_DIR, 'static')

    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
        'SQLALCHEMY_TRACK_MODIFICATIONS')

    CORS_ORIGIN_WHITELIST = [
        "http://127.0.0.1:5454"
    ]

    # if not os.path.exists(DIST_DIR):
    #     raise Exception('DIST_DIR not found: {}'.format(DIST_DIR))
