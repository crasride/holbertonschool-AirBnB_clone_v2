#!/usr/bin/python3
"""
That starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)


# you must remove the current SQLAlchemy Session
@app.teardown_appcontext
def close_session(exception):
    storage.close()


# display a HTML page: list of states
@app.route("/states_list", strict_slashes=False)
def states_list():
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
