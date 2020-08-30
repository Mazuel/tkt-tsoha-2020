import os

from messageforum import app
from messageforum.database import user_db, topic_db
from flask import redirect, render_template, request, session, flash, abort
from werkzeug.security import check_password_hash, generate_password_hash
from messageforum.routing import topic_routing, message_routing, thread_routing


@app.route("/")
def index():
    return redirect("/home")


@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    if user_db.fetch_user_if_exists(username) is None and len(username) >= 4 and len(password) >= 6:
        hash_value = generate_password_hash(password)
        user_db.add_user(username, hash_value)
    else:
        if len(username) < 4:
            flash("Username must be at least 4 characters long!")
        elif len(password) < 6:
            flash("Password must be at least 6 characters long!")
        else:
            flash(f"Username {username} already exists!")
        return redirect(request.referrer)
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
    user = user_db.fetch_user_if_exists(username)
    if user is None:
        flash("Incorrect username or password!")
        return redirect("/login")
    else:
        hash_value = user["password"]
        if check_password_hash(hash_value, password):
            session["username"] = username
            session["user.role"] = user["role_name"]
            session["csrf_token"] = os.urandom(16).hex()
            session["user.id"] = user["id"]
            print(session["user.role"])
            user_db.update_last_login(user["id"])
            return redirect("/home")
    flash("Incorrect username or password!")
    return redirect("/login")


@app.route("/logout")
def logout():
    del session["username"]
    del session["user.role"]
    del session["user.id"]
    del session["csrf_token"]
    return redirect("/home")


@app.route("/home")
def home():
    topics = topic_db.get_all_topics()
    return render_template("home.html", topics=topics)


@app.route("/profile/<username>")
def profile(username):
    user_data = user_db.fetch_user_for_profile_info(username)
    return render_template("profile.html", user=user_data, username=username)


@app.route("/user/updaterole/<int:user_id>", methods=["POST"])
def update_role(user_id):
    if session["csrf_token"] != request.form["csrf_token"]:
        return abort(403)
    new_role = request.form["role"]
    user_db.update_user_role(user_id, role_id=new_role)
    return redirect(request.referrer)


@app.route("/user/search", methods=["GET"])
def all_users():
    users = user_db.fetch_all_users()
    return render_template("users.html", users=users)


@app.route("/user/search", methods=["POST"])
def user_search():
    search_filter = request.form["username"]
    if len(search_filter) < 1:
        users = user_db.fetch_all_users()
    else:
        users = user_db.fetch_users_by_username(search_filter)
    return render_template("users.html", users=users)


def login_page():
    return render_template("login.html")
