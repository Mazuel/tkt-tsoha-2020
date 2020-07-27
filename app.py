from flask import Flask
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQL_ALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


@app.route("/")
def index():
    words = ["Monkey", "Banana", "Guitar"]
    return render_template("index.html", message="Welcome!", items=words)


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html", name=request.form["name"])
