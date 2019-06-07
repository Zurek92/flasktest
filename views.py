import random

from flask import Blueprint, redirect, render_template, request, url_for

from models import User, db

view = Blueprint('view', __name__)


@view.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        new_name = f'John{random.randint(100, 999)}'
        new_user = User(name=new_name)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('view.main_page'))
    users = User.query.all()
    return render_template('index.html', users=users)
