# project/__init__.py

import os
import datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


# Instantiate the app
app = Flask(__name__)

# Set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object('project.config.DevelopmentConfig')


# Instantiate the db
db = SQLAlchemy(app)


# A model
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    active = db.Column(db.Boolean(), default=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.created_at = datetime.datetime.utcnow()


# Routes
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

