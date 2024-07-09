DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255)
);

INSERT INTO users (email, password) VALUES ('email.1@gmail.com', 'Password_1');
INSERT INTO users (email, password) VALUES ('email.2@gmail.com', 'Password_2');
