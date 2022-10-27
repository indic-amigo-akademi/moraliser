import os
from flask import Flask, current_app, send_file, render_template
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from chat.api import api_bp
from chat.models import db, bcrypt, login_manager

migrate = Migrate()
csrf = CSRFProtect()


def create_app(test_config=None):
    # Initialise App and Config
    app = Flask(__name__)
    app.config.from_object('chat.config.Config')
    app.static_folder = app.config['STATIC_DIR']
    app.template_folder = app.config['DIST_DIR']

    import chat.models

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)
        bcrypt.init_app(app)
        login_manager.init_app(app)
        csrf.init_app(app)
        # db.create_all()

    # API Routes
    app.register_blueprint(api_bp)
    # app.logger.info('>>> {}'.format(Config.FLASK_ENV))

    @app.route('/')
    def index_client():
        # dist_dir = current_app.config['DIST_DIR']
        # entry = os.path.join(dist_dir, 'index.html')
        return render_template('index.html')

    return app
