# project/__init__.py

from flask import Flask, jsonify


# Instantiate the app
app = Flask(__name__)

# Set config
app.config.from_object('project.config.DevelopmentConfig')


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

