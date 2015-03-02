CREATE TABLE IF NOT EXISTS user_info(
    username VARCHAR(30),
    password TEXT,
    PRIMARY KEY(username)
);
CREATE TABLE IF NOT EXISTS user_secrets(
    username VARCHAR(30),
    secret TEXT,
    id SERIAL,
    PRIMARY KEY(id)
);
