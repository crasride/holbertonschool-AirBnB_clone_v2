#!/usr/bin/python3
"""
That starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""

from models import *
from flask import Flask
from models import storage
from flask import render_template


app = Flask(__name__)


# you must remove the current SQLAlchemy Session
@app.teardown_appcontext
def close_session(exception):
    storage.close()


# display a HTML page
@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ returns states of filters """
    states = storage.all("State")
    print ("hello")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == "__main__":
    # app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(host='0.0.0.0', port=5000, debug=True)
