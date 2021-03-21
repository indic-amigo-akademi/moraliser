import os
from flask import Flask, current_app, send_file

app = Flask(__name__, static_folder='../dist/static')

from .config import Config
# app.logger.info('>>> {}'.format(Config.FLASK_ENV))


@app.route('/')
def index_client():
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)
