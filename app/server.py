from flask import Flask
from .views import main_bp, fight_bp, choose_bp, errors_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    app.register_blueprint(fight_bp, url_prefix='/fight/')
    app.register_blueprint(choose_bp, url_prefix='/choose/')
    app.register_blueprint(errors_bp)
    return app
