import flask
from flask import request, jsonify

from dbhelper import get_tasks, create_task, delete_task

app = flask.Flask(__name__)
app.config["DEBUG"] = True


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
    task = data['task']
    delete_task(task)


