from messageforum.database.connection import db


def get_threads_by_id(topic_id):
    sql = "SELECT id, title, create_time, create_user, visible, (select count(*) as message_count from messages where thread_id = threads.id) FROM threads where topic_id=:topic_id"
    result = db.session.execute(sql, {"topic_id": topic_id})
    return result.fetchall()

