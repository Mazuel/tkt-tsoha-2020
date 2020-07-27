from messageforum.database.connection import db
from _datetime import datetime


def add_user(username, password):
    sql = "INSERT INTO users (username,password,role_id,create_time) VALUES (:username,:password,:role,:create_time)"
    db.session.execute(sql,
                       {"username": username, "password": password, "role": 3, "create_time": datetime.now()})
    db.session.commit()


def fetch_user_if_exists(username):
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    return user
