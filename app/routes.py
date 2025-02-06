from flask import Blueprint, render_template
from . import db
from .models import Task


main = Blueprint('main', __name__)


@main.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)
