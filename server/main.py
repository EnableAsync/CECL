from flask import Flask, request
from werkzeug.utils import secure_filename
from server.config.conf import STATIC_PATH
from server.client.task_controller_client import TaskController, Task

app = Flask(__name__)
tc = TaskController()


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
    create_time = request.form['create_time']
    union_train = request.form['union_train']
    edge_nodes = request.form['edge_nodes']
    file = request.form['file']
    tc.add_task(Task(
        name=name, create_time=create_time, union_train=union_train, edgenodes=edge_nodes, file=file
    ))


if __name__ == '__main__':
    app.run()
