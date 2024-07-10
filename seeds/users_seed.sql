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
    booked_dates DATE[],
    owner_id VARCHAR
    );

INSERT INTO spaces (description, name, bedrooms, price, country, city, booked_dates, owner_id) VALUES ('A lovely place to stay', 'Makers Mansion', 3, 100, 'UK', 'London', '{}', 'email.1@gmail.com');
INSERT INTO spaces (description, name, bedrooms, price, country, city, booked_dates, owner_id) VALUES ('A horrible place to stay', 'Makers Shed', 1, 5, 'UK', 'Burnley', '{}', 'email.1@gmail.com');
INSERT INTO spaces (description, name, bedrooms, price, country, city, booked_dates, owner_id) VALUES ('A fantastic holiday destination', 'Makers Villa', 1, 5000, 'USA', 'California', '{}', 'email.1@gmail.com');

DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS id_seq;
CREATE SEQUENCE IF NOT EXISTS id_seq;

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    spaces_id INT,
    requester_id INT,
    requested_dates DATE[],
    status VARCHAR(60)
    );

INSERT INTO bookings (spaces_id, requester_id, requested_dates, status) VALUES (1, 2, '{}', 'Pending');
INSERT INTO bookings (spaces_id, requester_id, requested_dates, status) VALUES (3, 2, '{}', 'Approved');