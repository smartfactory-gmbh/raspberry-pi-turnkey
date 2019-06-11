import subprocess
import signal
import string
import random
import re
import json
import time
import os
import socket
import requests

from flask import (
    Flask,
    request,
    send_from_directory,
    jsonify,
    render_template,
    redirect,
)

app = Flask(__name__, static_url_path="")

currentdir = os.path.dirname(os.path.abspath(__file__))
os.chdir(currentdir)

ssid_list = [
    "smartfactory",
    "smartmoo",
    "ok",
    "there is another one",
    "plus one",
    "internet 2.0",
    "the internet is here",
    "wow internet so cool",
    "wifi",
]


@app.route("/")
def main():
    return render_template("index.html", ssids=ssid_list)


@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)


@app.route("/languages/<path:path>")
def send_langauge(path):
    return send_from_directory("languages", path)


@app.route("/signin", methods=["POST"])
def signin():
    ssid = request.form["ssid"]
    password = request.form["password"]
    print(ssid, password)
    
    time.sleep(60000)
    return render_template("index.html", message="Please wait 2 minutes to connect.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, threaded=True)
