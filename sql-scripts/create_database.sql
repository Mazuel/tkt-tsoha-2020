create table user_account (
    id serial primary key,
    username varchar (50) unique not null,
    password varchar (50) not null,
    create_time timestamp not null,
    last_login timestamp
);
