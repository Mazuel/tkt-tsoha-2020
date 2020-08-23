from messageforum.database.connection import db


def get_messages(thread_topic):
    sql = "select id, message_content, create_time, (select username as user from users where id=create_user), visible from messages where thread_id=:thread_topic ORDER BY create_time ASC;"
    result = db.session.execute(sql, {"thread_topic": thread_topic})
    return result.fetchall()


def save_message(content, user_id, thread_name):
    sql = "INSERT INTO messages (message_content, thread_id, create_time, create_user) VALUES (:content, (select id from threads where title=:thread_name), NOW(), :user_id);"
    db.session.execute(sql, {"content": content, "thread_name": thread_name, "user_id": user_id})
    db.session.commit()