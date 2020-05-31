from flask import Flask, request
from werkzeug.utils import secure_filename
from server.config.conf import STATIC_PATH

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, It's CECL."


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['train']
    filename = secure_filename(f.filename)
    f.save(STATIC_PATH + filename)


@app.route('/task', methods=['POST'])
def add_task():
    name = request.form['name']