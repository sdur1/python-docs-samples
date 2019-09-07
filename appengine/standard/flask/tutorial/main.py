from flask import Flask, render_template, request
from models import *
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/translate", methods=["POST"])
def translate():
    # Get form information.
    sentence = request.form.get("line")

    word = sentence
    url = "https://wordsapiv1.p.rapidapi.com/words/"

    headers = {
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': "1586605e5emshcaee00a31ac29f1p1ad16djsn29fd93eb1a39"
        }

    response = requests.request("GET", url + word + "/synonyms", headers=headers)

    data = response.json()
    synonyms = data["synonyms"]
    print(synonyms)
    return render_template("error.html", message = synonyms[0])
