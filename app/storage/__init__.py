from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

from .database import models


def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)
    db.create_all(app=app)
