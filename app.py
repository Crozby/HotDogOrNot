import os
import random
import requests

from flask import Flask
from flask import render_template, request, jsonify

import network

app = Flask(__name__)
token = "12w1y2h3u12heu289HU2dsa&8789sak2ed"


@app.route('/')
def index():
    return render_template("main.html")


@app.route('/get_answer', methods=["POST"])
def get_answer():
    image_path = request.form.get("path")
    tkn = request.form.get("token")
    if tkn == token and type(image_path) is str and image_path[-3:] == "jpg":
        img = requests.get(image_path)
        if img.status_code != 200:
            return jsonify(error=True)
        path = "tmp/" + str(random.randint(1, 100000000)) + ".jpg"
        out = open(path, "wb")
        out.write(img.content)
        out.close()
        if network.get_prediction(path):
            answer = "Hot dog!"
        else:
            answer = "There is NO hot dog"
        if os.path.isfile(path):
            os.remove(path)
        return jsonify(answer=answer, image=image_path)
    else:
        return jsonify(error=True)


if __name__ == '__main__':
    app.run()
