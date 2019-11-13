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

from pathlib import Path

from flask import (
    Flask,
    request,
    make_response,
    send_from_directory,
    jsonify,
    render_template,
    redirect,
)

app = Flask(__name__, static_url_path="")

lang_file_folder = str(Path.home()) + "/.config/iqube/"
lang_file_path = lang_file_folder + "language.config"

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
    language = open(lang_file_path, 'r').read().strip()
    return render_template("index.html", ssids=ssid_list, language=language)

@app.route("/iqube/<string:language>/<int:step>")
def iqube(language, step):
    return render_template(
        "language.html", 
        language=language,
        step=step
    )

@app.route("/configure")
def configure_via_iqube():
    language = open(lang_file_path, 'r').read().strip()
    return render_template("configure_via_pi.html", ssids=ssid_list, language=language)

@app.route("/language", methods=["POST"])
def setLanguage():
    lang = request.form["language"];
    
    with open(lang_file_path, 'w') as f:
        f.write(lang)

    return make_response(
        lang,
        200
    )

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
    # create language configuration if it does not exist yet

    if not os.path.isfile(lang_file_path):
        if not os.path.exists(lang_file_folder):
            os.makedirs(lang_file_folder)
        with open(lang_file_path, "w") as f: 
            f.write("de") # put in default language

    app.run(host="0.0.0.0", port=80, threaded=True)

