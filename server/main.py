import os

import flask


localdir = os.path.abspath(os.path.dirname(__file__))
app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.send_file("site/main.html")


@app.route("/<filepath>/")
def returnFile(filepath):
    """ Attempt to return files from site from their equivalent path at the
    root (/main.html -> /site/main.html) """
    testpath = os.path.join(localdir, "site/" + filepath)
    if os.path.exists(testpath):
        return flask.send_from_directory("site", filepath)
    else:
        flask.abort(404)

if __name__ == "__main__":
    app.run(debug=True)
