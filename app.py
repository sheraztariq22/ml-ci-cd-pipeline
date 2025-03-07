import flask

app = flask.Flask(__name__)


def hello():
    return "Hello, World!"
