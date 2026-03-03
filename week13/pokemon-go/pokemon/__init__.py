import os
from flask import Flask
from .extensions import db
from .core import core_bp
from .pokemon import pokemon_bp
from .users import users_bp

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config["SECRET_KEY"] = "dev"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pokemon.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(core_bp)
    app.register_blueprint(pokemon_bp)
    app.register_blueprint(users_bp)

    return app