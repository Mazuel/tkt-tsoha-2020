from messageforum.database.connection import db


def get_threads_by_id(topic_id):
    sql = "SELECT * FROM threads where topic_id=:topic_id"
    result = db.session.execute(sql, {"topic_id": topic_id})
    return result.fetchall()
