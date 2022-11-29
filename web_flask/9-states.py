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


# display a HTML page
@app.route("/states", strict_slashes=False)
@app.route("/states/<state_id>", strict_slashes=False)
def states(state_id=None):
    """
    displays all states or cities by state id
    """
    if state_id is None:
        states = storage.all("State")

    else:
        states = storage.all("State")
        state_id = "State." + state_id

    return render_template('9-states.html', states=states, state_id=state_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
