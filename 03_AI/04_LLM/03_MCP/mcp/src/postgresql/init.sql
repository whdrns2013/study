CREATE TABLE address_book (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    email VARCHAR(100),
    group_name VARCHAR(100)
);

INSERT INTO address_book (name, email, group_name)
VALUES ('홍길동', 'hong@hong.hong', 'korea');

INSERT INTO address_book (name, email, group_name)
VALUES ('세종대왕', 'sejoing@king.josun', 'korea');

INSERT INTO address_book (name, email, group_name)
VALUES ('존윅', 'john@unknown.com', 'usa');