create table roles (
    id serial primary key,
    role_name varchar (50) not null
);

create table user_account (
    id serial primary key,
    username varchar (50) unique not null,
    password varchar (50) not null,
    role_id integer references roles,
    create_time timestamp not null,
    last_login timestamp
);

create table subject (
    id serial primary key,
    subject_name varchar (50) not null,
    create_time timestamp not null,
    last_change_user integer references user_account
);

create table thread_messages (
    thread_id integer references thread,
    message_id integer references message
);

create table thread (
    id serial primary key,
    title varchar (50) not null,
    messages integer references thread_messages,
    create_time timestamp not null,
    create_user integer references user_account
);

