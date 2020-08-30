from messageforum import app
from messageforum.database import message_db, thread_db
from flask import redirect, request, session, flash, render_template, abort


@app.route("/new-message/<int:thread_id>", methods=["POST"])
def new_message(thread_id):
    if session["csrf_token"] != request.form["csrf_token"]:
        return abort(403)
    if thread_db.thread_exists_by_id(thread_id) is False:
        flash("That thread does not exist!")
        return redirect("/home")
    content = request.form["message_content"]
    if len(content) < 1:
        flash("Message must not be empty!")
        return redirect(request.referrer)
    elif len(content) > 1500:
        flash("Message is too long!")
        return redirect(request.referrer)
    message_db.save_message(content, session["user.id"], thread_id)
    return redirect(request.referrer)


@app.route("/topic/<topic>/<thread>/<int:thread_id>")
def messages_for_thread(topic, thread, thread_id):
    messages = message_db.get_messages(thread_id)
    return render_template("messages.html", topic=topic, thread=thread, messages=messages, thread_id=thread_id)


@app.route("/message/delete/<int:message_id>", methods=["POST"])
def delete_message(message_id):
    message_db.delete(message_id)
    return redirect(request.referrer)
