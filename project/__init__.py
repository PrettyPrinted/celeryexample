
from flask import Flask

from .extensions import db, c
from .views import main

def create_app():
    app = Flask(__name__)
    app.config.update(CELERY_CONFIG={
        'broker_url': 'redis://redis',
        'result_backend': 'redis://redis'
    })

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SECRET_KEY"] = "IAMTHEONEWHOKNOCKS"

    c.init_app(app)
    db.init_app(app)

    app.register_blueprint(main)



    return app, c.celery