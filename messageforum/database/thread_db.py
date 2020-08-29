from messageforum.database.connection import db


def get_threads_by_id(topic_id):
    sql = "SELECT id, title, create_time, create_user, visible, (select count(*) as message_count from messages where thread_id = threads.id) FROM threads where topic_id=:topic_id;"
    result = db.session.execute(sql, {"topic_id": topic_id})
    return result.fetchall()


def add_thread(title, topic_title, create_user):
    sql = "INSERT INTO threads (title, topic_id, create_time, create_user) VALUES (:title, (select id from topics where topic_title=:topic_title), NOW(), :create_user)"
    db.session.execute(sql, {"title": title, "topic_title": topic_title, "create_user": create_user})
    db.session.commit()


def thread_exists(topic_id, title):
    for thread in get_threads_by_id(topic_id):
        if thread['title'] == title:
            return True
    return False
