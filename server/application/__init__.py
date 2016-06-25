""" The main pythonista.cloud application. Contains the basic logic for
pythonista.cloud. """

import os

import flask

localdir = os.path.abspath(os.path.dirname(__file__))
staticdir = os.path.join(localdir, "../static")

app = flask.Flask(__name__)


@app.route("/")
def index():
    """ Return the main page (from /site/main.html) for requests to the file
    root """
    return flask.send_file(os.path.join(staticdir, "main.html"))


@app.route("/<filepath>/")
def returnFile(filepath):
    """ Attempt to return files from site from their equivalent path at the
    root (/main.html -> /site/main.html) """
    testpath = os.path.join(staticdir, filepath)
    if os.path.exists(testpath):
        return flask.send_from_directory(staticdir, filepath)
    else:
        flask.abort(404)

if __name__ == "__main__":
    app.run(debug=True)
