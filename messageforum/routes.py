from messageforum import app
from messageforum.database import user_repository, topic_repository, thread_repository
from flask import redirect, render_template, request, session, flash
from werkzeug.security import check_password_hash, generate_password_hash


@app.route("/")
def index():
    return redirect("/home")


@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    if user_repository.fetch_user_if_exists(username) is None and len(username) >= 4 and len(password) >= 6:
        hash_value = generate_password_hash(password)
        user_repository.add_user(username, hash_value)
    else:
        # Todo: show correct error message if invalid username
        if len(username) < 4:
            flash("Username must be at least 4 characters long!")
        elif len(password) < 6:
            flash("Password must be at least 6 characters long!")
        else:
            flash(f"Username {username} already exists!")
        return redirect("/register")
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
        flash("Incorrect username or password!")
        return redirect("/login")
    else:
        hash_value = user["password"]
        if check_password_hash(hash_value, password):
            session["username"] = username
            session["user.role"] = user["role_name"]
            session["user.id"] = user["id"]
            user_repository.update_last_login(user["id"])
            return redirect("/home")
    flash("Incorrect username or password!")
    return redirect("/login")


@app.route("/logout")
def logout():
    del session["username"]
    del session["user.role"]
    del session["user.id"]
    return redirect("/home")


@app.route("/home")
def home():
    topics = topic_repository.get_all_topics()
    return render_template("home.html", topics=topics)


@app.route("/new-topic", methods=["POST"])
def new_topic():
    if session["username"]:
        title = request.form["title"]
        if topic_repository.fetch_topic_by_title(title) is None:
            topic_repository.add_topic(title, session["user.id"])
        else:
            print(f"Topic {title.upper()} already exists!")
    return redirect("/home")


@app.route("/profile/<username>")
def profile(username):
    user_data = user_repository.fetch_user_for_profile_info(username)
    return render_template("profile.html", user=user_data, username=username)


@app.route("/<title>/<int:id_>/threads")
def threads_for_topic(title, id_):
    threads = thread_repository.get_threads_by_id(id_)
    return render_template("threads.html", threads=threads, topic_title=title, id_=id_)


@app.route("/<topic>/<int:id_>/threads/<thread>")
def messages_for_thread(topic, thread, id_):
    return render_template("messages.html", topic=topic, thread=thread)


def login_page():
    return render_template("login.html")
