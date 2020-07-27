from messageforum.app import app
import messageforum.database.user_repository as user_repository
from flask import redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    if user_repository.fetch_user_if_exists(username) is None:
        hash_value = generate_password_hash(password)
        user_repository.add_user(username, hash_value)
    else:
        print(username, password)

    return redirect("/login")


@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")


@app.route("/register", methods=["GET"])
def register_page():
    return render_template("register.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    user = user_repository.fetch_user_if_exists(username)
    if user is None:
        print()
        # TODO: invalid username
    else:
        hash_value = user[0]
        if check_password_hash(hash_value, password):
            session["username"] = username
            return redirect("/home")
            # TODO: correct username and password
        else:
            print()
            return redirect("/login")
            # TODO: invalid password


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")


@app.route("/home")
def home():
    return render_template("home.html")


def login_page():
    return render_template("login.html")
