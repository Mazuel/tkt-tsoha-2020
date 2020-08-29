from messageforum import app
from messageforum.database import user_db, topic_db, thread_db, message_db
from flask import redirect, render_template, request, session, flash
from werkzeug.security import check_password_hash, generate_password_hash


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
    user = user_db.fetch_user_if_exists(username)
    if user is None:
        flash("Incorrect username or password!")
        return redirect("/login")
    else:
        hash_value = user["password"]
        if check_password_hash(hash_value, password):
            session["username"] = username
            session["user.role"] = user["role_name"]
            session["user.id"] = user["id"]
            user_db.update_last_login(user["id"])
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
    topics = topic_db.get_all_topics()
    return render_template("home.html", topics=topics)


@app.route("/new-topic", methods=["POST"])
def new_topic():
    if session["username"]:
        title = request.form["title"]
        if len(title) < 1:
            flash("Title must not be empty!")
            return redirect(request.referrer)
        if topic_db.fetch_topic_by_title(title) is None:
            topic_db.add_topic(title, session["user.id"])
        else:
            flash("Topic already exists!")
    return redirect(request.referrer)


@app.route("/profile/<username>")
def profile(username):
    user_data = user_db.fetch_user_for_profile_info(username)
    return render_template("profile.html", user=user_data, username=username)


@app.route("/<title>/<int:id_>")
def threads_for_topic(title, id_):
    threads = thread_db.get_threads_by_id(id_)
    return render_template("threads.html", threads=threads, topic_title=title, topic_id=id_)


@app.route("/<topic>/<thread>/<int:thread_id>")
def messages_for_thread(topic, thread, thread_id):
    messages = message_db.get_messages(thread_id)
    return render_template("messages.html", topic=topic, thread=thread, messages=messages, thread_id=thread_id)


@app.route("/new-thread/<topic_title>", methods=["POST"])
def new_thread(topic_title):
    print(topic_title)
    if session["username"]:
        title = request.form["title"]
        user_id = session["user.id"]
        if len(title) < 1:
            flash("Title must not be empty!")
            return redirect(request.referrer)
        thread_db.add_thread(title, topic_title, user_id)
    return redirect(request.referrer)


@app.route("/new-message/<thread_title>", methods=["POST"])
def new_message(thread_title):
    if session["username"]:
        content = request.form["message_content"]
        if len(content) < 1:
            flash("Message must not be empty!")
            return redirect(request.referrer)
        elif len(content) > 1500:
            flash("Message is too long!")
            return redirect(request.referrer)
        message_db.save_message(content, session["user.id"], thread_title)
    return redirect(request.referrer)


def login_page():
    return render_template("login.html")
