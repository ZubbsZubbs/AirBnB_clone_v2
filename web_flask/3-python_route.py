#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB! in browser"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """returns C is fun"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """returns python is magic"""
    return 'Python {}'.format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
