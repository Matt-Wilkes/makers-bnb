DROP TABLE IF EXISTS spaces;

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
