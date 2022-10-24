import os
from flask import Flask, current_app, send_file
from flask_sqlalchemy import SQLAlchemy
from .api import api_bp

# Initialise App and Config
app = Flask(__name__, static_folder='../dist/static')
app.config.from_object('chat.config.Config')

db = SQLAlchemy(app)

# API Routes
app.register_blueprint(api_bp)
# app.logger.info('>>> {}'.format(Config.FLASK_ENV))


@app.route('/')
def index_client():
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)
