import flask
import flask_shelve
import shelve
from flask import request
import json


with shelve.open('shelve.db') as db:
    with open('initData.json') as f:
        mydict = json.load(f)
        db.update(mydict)


app = flask.Flask(__name__)
app.config['SHELVE_FILENAME'] = 'shelve.db'
flask_shelve.init_app(app)


@app.route('/monkey_detection', methods=['GET', 'POST'])
def md():
    db = flask_shelve.get_shelve('c', )

    camera_details = db[request.form['camera']]
    camera_details['status'] = True if request.form['status'] == "True" else False
    db[request.form['camera']] = camera_details

    return 'OK'


@app.route('/', methods=['GET', 'POST'])
def index():
    db = flask_shelve.get_shelve('c')
    return json.dumps(dict(db))


if __name__ == '__main__':
    app.run()
