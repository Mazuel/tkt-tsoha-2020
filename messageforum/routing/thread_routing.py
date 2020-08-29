from messageforum import app
from messageforum.database import thread_db
from flask import redirect, render_template, request, session, flash


@app.route("/new-thread/<int:topic_id>/<topic_title>", methods=["POST"])
def new_thread(topic_id, topic_title):
    if session["username"]:
        title = request.form["title"]
        user_id = session["user.id"]
        if len(title) < 1:
            flash("Title must not be empty!")
            return redirect(request.referrer)
        if thread_db.thread_exists(topic_id, title):
            flash(f"Topic already contains thread: {title}")
            return redirect(request.referrer)
        thread_db.add_thread(title, topic_title, user_id)
    return redirect(request.referrer)


@app.route("/<title>/<int:id_>")
def threads_for_topic(title, id_):
    threads = thread_db.get_threads_by_id(id_)
    return render_template("threads.html", threads=threads, topic_title=title, topic_id=id_)
