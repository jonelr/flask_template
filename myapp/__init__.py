from flask import Flask

from myapp.auth.routes import auth_bp
from myapp.auth.extensions import bcrypt, login_manager
from myapp.site.routes import site_bp
from myapp.models import db, migrate


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py', silent=True)

    app.register_blueprint(auth_bp)
    app.register_blueprint(site_bp)

    bcrypt.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    return app
