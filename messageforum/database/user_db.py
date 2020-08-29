from messageforum.database.connection import db


def add_user(username, password):
    sql = "INSERT INTO users (username,password,role_id,create_time) VALUES (:username,:password,:role,NOW());"
    db.session.execute(sql,
                       {"username": username, "password": password, "role": 3})
    db.session.commit()


def fetch_user_if_exists(username):
    sql = "select u.id, username, password, r.role_name from users u INNER JOIN roles as r on role_id = r.id WHERE u.username=:username;"
    result = db.session.execute(sql, {"username": username})
    return result.fetchone()


def fetch_user_for_profile_info(username):
    sql = "select u.username, r.role_name, u.create_time, u.last_login from users u INNER JOIN roles as r on role_id = r.id WHERE u.username=:username;"
    result = db.session.execute(sql, {"username": username})
    return result.fetchone()


def update_last_login(id_):
    sql = "UPDATE users set last_login = NOW() WHERE id=:id;"
    db.session.execute(sql, {"id": id_})
    db.session.commit()
