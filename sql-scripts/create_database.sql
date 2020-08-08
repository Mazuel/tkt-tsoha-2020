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

create table subjects (
    id serial primary key,
    subject_name varchar (50) not null,
    create_time timestamp not null,
    create_user integer references users,
    visible boolean default false
);

create table threads (
    id serial primary key,
    title varchar (50) not null,
    messages integer references messages,
    create_time timestamp not null,
    create_user integer references users,
    visible boolean default false
);

create table messages (
    id serial primary key,
    message_content TEXT not null,
    create_time timestamp not null,
    create_user integer references users,
    visible boolean default false
)

