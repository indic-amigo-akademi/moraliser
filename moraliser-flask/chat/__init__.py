import os
from flask import Flask, current_app, send_file, render_template, jsonify, Response
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from chat.api import api_bp
from chat.models import db, bcrypt, login_manager
from flask_cors import CORS

migrate = Migrate()
csrf = CSRFProtect()
cors = CORS()


def create_app(test_config=None) -> Flask:
    # Initialise App and Config
    app = Flask(__name__)
    app.config.from_object("chat.config.Config")
    # app.static_folder = app.config['STATIC_DIR']
    # app.template_folder = app.config['DIST_DIR']

    import chat.models

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)
        bcrypt.init_app(app)
        login_manager.init_app(app)
        csrf.init_app(app)
        cors.init_app(app)
        # db.create_all()

    # API Routes
    app.register_blueprint(api_bp)
    # app.logger.info('>>> {}'.format(Config.FLASK_ENV))

    # @app.before_request
    # def set_xsrf_cookie() -> Response:
    #     response.set_cookie("csrf_token", generate_csrf())
    #     return response

    @app.route("/", methods=["GET"])
    def index() -> Response:
        return jsonify(
            {"success": True, "message": "Moraliser server is up and running!🖥️"}
        )

    # def index_client():
    # dist_dir = current_app.config['DIST_DIR']
    # entry = os.path.join(dist_dir, 'index.html')
    # return render_template('index.html')

    return app
