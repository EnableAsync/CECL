from flask import Flask, request
from werkzeug.utils import secure_filename
from server.config.conf import STATIC_PATH
from server.client.task_controller_client import TaskController, Task
from server.client.data_manger_client import DataManager
from server.client.task_runtime_client import TaskRuntime
from flask_cors import CORS
import json
import message_hub.client.deploy_controller_client
import message_hub.client.deploy_runtime_client

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

tc = TaskController()
dm = DataManager()
tr = TaskRuntime()

dc = message_hub.client.deploy_controller_client.TaskController()
dr = message_hub.client.deploy_runtime_client.TaskRuntime()


@app.route('/')
def hello():
    return "Hello, It's CECL."


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['train']
    filename = secure_filename(f.filename)
    f.save(STATIC_PATH + filename)
    return {'code': 0, 'msg': 'success'}


@app.route('/task', methods=['POST'])
def add_task():
    name = request.form['name']
    create_time = int(request.form['create_time'])
    union_train = int(request.form['union_train'])
    edge_nodes = request.form['edge_nodes']
    file = request.form['file']
    print(file)
    t: Task = Task(
        name=name, create_time=create_time, union_train=union_train, edgenodes=edge_nodes, file=file
    )
    task_id: int = json.loads(tc.add_task(t).resp.message)['id']
    t.task_id = task_id
    f = open(STATIC_PATH + file, 'rb')
    resp = tr.upload_task(t, f.read(), b'').resp
    print(resp)
    return {'code': tc.start_task(task_id).resp.code}


@app.route('/stop', methods=['GET'])
def stop_task():
    task_id = request.form['task_id']
    return {'code': tc.stop_task(int(task_id)).resp.code}


@app.route('/task', methods=['GET'])
def get_tasks():
    resp = dm.get_all_tasks().resp
    return {'code': resp.code, 'msg': resp.message}


@app.route('/task/log/<task_id>', methods=['GET'])
def get_task_log(task_id):
    resp = dm.get_task_log(int(task_id)).resp
    return {'code': resp.code, 'msg': resp.message}


@app.route('/task/deploy/<task_id>', methods=['GET'])
def deploy(task_id):
    model_name = request.form['model']
    print('get file:{}/{}'.format(task_id, model_name))

    # get model file
    model_task = Task(task_id=task_id, file=model_name)
    resp = tr.get_file(model_task)
    if resp.resp.code != 0:
        print("get model file fail")
        return {'code': resp.resp.code, 'msg': resp.resp.message}
    model_file = resp.script

    # upload model file
    resp = dr.upload_task(model_task, model_file, b'').resp
    print(resp)
    if resp.resp.code != 0:
        print("upload model file fail")
        return {'code': resp.resp.code, 'msg': resp.resp.message}

    # create model task
    name = request.form['name']
    create_time = int(request.form['create_time'])
    file = request.form['file']
    print(file)
    t: Task = Task(
        name=name, create_time=create_time, file=file
    )
    task_id: int = json.loads(dc.add_task(t).resp.message)['id']
    t.task_id = task_id
    f = open(STATIC_PATH + file, 'rb')

    # upload model predict script
    resp = dr.upload_task(t, f.read(), b'').resp
    print(resp)

    # start model
    return {'code': dc.start_task(task_id).resp.code}


if __name__ == '__main__':
    app.run()
