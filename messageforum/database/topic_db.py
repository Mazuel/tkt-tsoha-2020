from messageforum.database.connection import db


def fetch_topic_by_title(title):
    sql = "SELECT * FROM topics where LOWER(topic_title)=LOWER(:topic_title)"
    result = db.session.execute(sql, {"topic_title": title})
    return result.fetchone()


def add_topic(title, user_id):
    sql = "INSERT INTO topics (topic_title, create_time, create_user, visible) VALUES (:topic_title, NOW(), :create_user, :visible);"
    db.session.execute(sql, {"topic_title": title, "create_user": user_id, "visible": True})
    db.session.commit()


def get_all_topics():
    sql = "SELECT id, topic_title, create_time, (SELECT username as create_user FROM users WHERE id = create_user), visible, (select count(*) as thread_count from threads where topic_id = topics.id) FROM topics;"
    result = db.session.execute(sql)
    return result.fetchall()
