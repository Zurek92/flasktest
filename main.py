#!/usr/bin/env python3
from flask import Flask

from models import db
from views import view

app = Flask(__name__)
app.register_blueprint(view)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'somesecretkey'

db.init_app(app)

if __name__ == '__main__':
    app.run()
