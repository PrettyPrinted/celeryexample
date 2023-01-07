from flask import Blueprint, render_template, redirect, request

from .tasks import count
from .forms import MyForm

main = Blueprint('main', __name__)

@main.route('/start')
def start():
    task = count.delay()
    return render_template('start.html', task=task)

@main.route('/form', methods=['GET', 'POST'])
def submit():
    form = MyForm()
    print("DATA", form.name.data)
    if form.validate_on_submit():
        print("YO NAME IS: ", form.name.data)

        count.delay(form.data)
        return redirect('/form')
    return render_template('form.html', form=form)

@main.route('/cancel/<task_id>')
def cancel(task_id):
    task = count.AsyncResult(task_id)
    task.abort()
    return 'Canceled!'