import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.send_file("site/main.html")


@app.route("/main.<ext>")
def assetFile(ext):
    return flask.send_from_directory("site", "main." + ext)


@app.route("/particleground.min.js")
def assertFile():
    return flask.send_file("site/particleground.min.js")

if __name__ == "__main__":
    app.run(debug=True)
