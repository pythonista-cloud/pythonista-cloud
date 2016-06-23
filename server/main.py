from flask import Flask, send_file, send_from_directory
import sys

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("site/main.html")

@app.route("/main.<ext>")
def assetFile(ext):
    return send_from_directory("site", "main."+ext)

@app.route("/particleground.min.js")
def assertFile():
    return send_file("site/particleground.min.js")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
