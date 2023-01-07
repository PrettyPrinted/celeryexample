from flask import Flask, render_template, current_app
from time import sleep
from .extensions import c, db
from celery.contrib.abortable import AbortableTask

from .forms import MyForm

from .models import User

@c.celery.task(bind=True, base=AbortableTask)
def count(self, form_data):



    db.session.add(User(name=form_data['name']))
    db.session.commit()

    

    for i in range(10):
        if self.is_aborted():
            return 'Task stopped!'
        print(i)
        sleep(1)
    return 'DONE!' 
