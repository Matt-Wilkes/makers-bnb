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

-- Spaces table -- original from 'space.sql' from George's commit 
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS id_seq;
CREATE SEQUENCE IF NOT EXISTS id_seq;

CREATE TABLE spaces(
    id SERIAL PRIMARY KEY,
    description VARCHAR(60),
    name VARCHAR(60),
    bedrooms INTEGER,
    price INTEGER,
    country VARCHAR(60),
    city VARCHAR(60),
    booked_dates DATE[]
    );

INSERT INTO spaces (users_id, description, name, bedrooms, price, country, city, booked_dates) VALUES (1, 'A lovely place to stay', 'Makers Mansion', 3, 100, 'UK', 'London', '{}');
INSERT INTO spaces (users_id, description, name, bedrooms, price, country, city, booked_dates) VALUES (2, 'A horrible place to stay', 'Makers Shed', 1, 5, 'UK', 'Burnley', '{}');
INSERT INTO spaces (users_id, description, name, bedrooms, price, country, city, booked_dates) VALUES (1, 'A fantastic holiday destination', 'Makers Villa', 1, 5000, 'USA', 'California', '{}');


-- original space.sql
"""DROP TABLE IF EXISTS spaces;

-- Then, we recreate them
CREATE TABLE spaces(
    id SERIAL PRIMARY KEY,
    description VARCHAR(60),
    name VARCHAR(60),
    bedrooms INTEGER,
    price INTEGER,
    country VARCHAR(60),
    city VARCHAR(60),
    booked_dates DATE[]
    );

INSERT INTO spaces (description, name, bedrooms, price, country, city, booked_dates) VALUES ('A lovely place to stay', 'Makers Mansion', 3, 100, 'UK', 'London', '{}');
"""