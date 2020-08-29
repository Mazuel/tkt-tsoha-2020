create table roles (
    id serial primary key,
    role_name varchar (50) not null
);

create table users (
    id serial primary key,
    username TEXT UNIQUE,
    password TEXT,
    role_id integer references roles,
    create_time timestamp not null,
    last_login timestamp
);

create table topics (
    id serial primary key,
    topic_title varchar (50) not null,
    create_time timestamp not null,
    create_user integer references users,
    visible boolean default true
);

create table threads (
    id serial primary key,
    title varchar (50) not null,
    topic_id integer references topics,
    create_time timestamp not null,
    create_user integer references users,
    visible boolean default true
);

create table messages (
    id serial primary key,
    message_content TEXT not null,
    thread_id integer references threads,
    create_time timestamp not null,
    create_user integer references users,
    visible boolean default true
);

INSERT INTO roles (role_name) values ('ADMIN');
INSERT INTO roles (role_name) values ('MODERATOR');
INSERT INTO roles (role_name) values ('USER');


