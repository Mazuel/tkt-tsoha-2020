from messageforum import app
from messageforum.database import topic_db
from flask import redirect, request, session, flash


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
