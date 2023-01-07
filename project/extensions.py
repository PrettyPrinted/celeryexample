from celery import Celery
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MyCelery:
    def __init__(self, app=None):
        self.celery = Celery(__name__) # app.name

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        
        self.celery.conf.update(app.config["CELERY_CONFIG"])

        class ContextTask(self.celery.Task):
            def __call__(self, *args, **kwargs):
                with app.app_context():
                    return self.run(*args, **kwargs)

        self.celery.Task = ContextTask

c = MyCelery()