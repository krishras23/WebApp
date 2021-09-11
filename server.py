import flask
from flask import request, jsonify
from flask_cors import CORS
from dbhelper import get_tasks, create_task, delete_task, update_task

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route('/', methods=['GET'])
def show_tasks():
    all_tasks = get_tasks()
    task_dict = {}
    i = 1
    z = 0
    for x in all_tasks:
        task_dict[i] = all_tasks[z]
        i = i + 1
        z = z + 1
    return jsonify(task_dict)


@app.route('/create_task', methods=['POST'])
def task_creation():
    data = request.get_json()
    task = data['task']
    importance = data['importance']
    owner = data['owner']
    create_task(task, importance, owner)
    return ""


@app.route('/delete', methods=['DELETE'])
def task_deletion():
    data = request.get_json()
    importance = data['importance']
    delete_task(importance)
    return ""


@app.route('/update_task', methods=['PATCH'])
def updating_task():
    data = request.get_json()
    old_owner = data['old_owner']
    new_owner = data['new_owner']
    update_task(old_owner, new_owner)
    return ""


@app.route('/return_id', methods=['POST'])
def returning_id():
    data = request.get_json()


app.run()
