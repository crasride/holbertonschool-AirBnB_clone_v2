#!/usr/bin/python3
"""
That starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


# /c/<text>: display “C ” (replace underscore _ symbols with a space)
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace('_', ' ')
    return "C {}".format(text)


# /python/<text>: value “is cool” display “Python ” (replace '_' by ' ')
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    text = text.replace('_', ' ')
    return "Python {}".format(text)


# /number/<n>: display “n is a number” only if n is an integer
@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    return "{} is a number".format(n)


# /number_template/<n>: display a HTML page only if n is an integer
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_s(n):
    return render_template("5-number.html", n=n)


# /number_odd_or_even/<n> display a HTML page only if n is an integer
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_s(n):
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
