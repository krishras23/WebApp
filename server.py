import flask
from flask import redirect, url_for, request
from flask import jsonify

from dbhelpler import get_databases

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def trello():
    list_of_databases = get_databases()
    dict_db = {}
    i = 1
    z = 0
    for x in list_of_databases:
        dict_db[i] = list_of_databases[z]
        i = i + 1
        z = z + 1
    return jsonify(dict_db)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s to the party' % name


# decorator method
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


@app.route('/requestingjson', methods=['POST'])
def requestingjson():
    data = request.get_json()
    name = data['name'] + "joe"
    location = data['location']
    occupation = data['occupation']
    random_dude = data['family']
    more_random = random_dude[2]
    print(random_dude)
    return ''


app.run()
