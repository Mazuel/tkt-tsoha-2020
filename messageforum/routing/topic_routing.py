from messageforum import app
from messageforum.database import topic_db, thread_db
from flask import redirect, request, session, flash, abort


@app.route("/new-topic", methods=["POST"])
def new_topic():
    if session["csrf_token"] != request.form["csrf_token"]:
        return abort(403)
    title = request.form["title"]
    if len(title) < 1:
        flash("Title must not be empty!")
        return redirect(request.referrer)
    if topic_db.fetch_topic_by_title(title) is None:
        topic_db.add_topic(title, session["user.id"])
    else:
        flash("Topic already exists!")
    return redirect(request.referrer)


@app.route("/topic/delete/<int:id_>", methods=["POST"])
def delete_topic(id_):
    if session["csrf_token"] == request.form["csrf_token"] and session["user.role"] == "ADMIN":
        topic_db.delete_topic(id_)
        thread_db.delete_threads_by_topic(id_)
        return redirect(request.referrer)
    else:
        return abort(401, description="You have no permission to delete threads!")
