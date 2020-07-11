-- init & set db
DROP DATABASE IF EXISTS alpha;
CREATE DATABASE alpha;
\c alpha

-- 
-- init `users` schema
--
DROP TABLE IF EXISTS users;
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(25) NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- `users` dummy data
INSERT INTO users (id, username, password) VALUES (DEFAULT, 'dummy username', 'dummy password');

-- 
-- init `product_apis` schema
--
DROP TABLE IF EXISTS product_apis;
CREATE TABLE product_apis(
    id SERIAL PRIMARY KEY,
    provider VARCHAR NOT NULL
);

-- `product_apis` dummy data
INSERT INTO product_apis (id, provider) VALUES (DEFAULT, 'dummy provider');
INSERT INTO product_apis (id, provider) VALUES (DEFAULT, 'dummy provider 2');

-- 
-- init `products` schema
--
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    api_id INTEGER NOT NULL,
    product_id VARCHAR NOT NULL,
    name VARCHAR NOT NULL,
    price REAL NOT NULL,
    rating REAL NOT NULL,
    producer VARCHAR NOT NULL,
    FOREIGN KEY (api_id) REFERENCES product_apis (id) ON DELETE CASCADE
);

-- `products` dummy data
INSERT INTO products
    (id, api_id, product_id, name, price, rating, producer)
    values (DEFAULT, 1, 'D: productrod id', 'D: name', 10.45, 8.9, 'D: producer');
INSERT INTO products
    (id, api_id, product_id, name, price, rating, producer)
    values (DEFAULT, 2, 'D: productrod id 2', 'D: name 2', 10.45, 8.9, 'D: producer');

-- 
-- init `product_photos` schema
--
DROP TABLE IF EXISTS product_photos;
CREATE TABLE product_photos (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL,
    api_id INTEGER NOT NULL,
    photo_id VARCHAR NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE,
    FOREIGN KEY (api_id) REFERENCES product_apis (id) ON DELETE CASCADE
);
-- `product_photos` dummy data
INSERT INTO product_photos
    (id, product_id, api_id, photo_id)
    values (DEFAULT, 2, 2, 'dummy photo id');
INSERT INTO product_photos
    (id, product_id, api_id, photo_id)
    values (DEFAULT, 1, 2, 'dummy photo id 2');

-- 
-- init `lists` schema
--
DROP TABLE IF EXISTS lists;
CREATE TABLE lists (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    title VARCHAR(50) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);
-- `lists` dummy data
INSERT INTO lists (id, user_id, title) values (DEFAULT, 1, 'dummy title');

-- 
-- init `list_entries` schema
--
DROP TABLE IF EXISTS list_entries;
CREATE TABLE list_entries (
    list_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    index INTEGER NOT NULL,
    body VARCHAR(2000) NOT NULL,
    rating REAL NOT NULL,
    photo_id INTEGER,
    FOREIGN KEY (list_id) REFERENCES lists (id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products (id),
    FOREIGN KEY (photo_id) REFERENCES product_photos (id)
);
-- `list_entries` dummy data
INSERT INTO list_entries (list_id, product_id, index, body, rating, photo_id) values (1, 1, 0, 'D: body', 7.3, 1);

-- 
-- init `list_likes` schema
--
DROP TABLE IF EXISTS list_likes;
CREATE TABLE list_likes (
    list_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (list_id) REFERENCES lists (id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);
-- `list_likes` dummy data
INSERT INTO list_likes (list_id, user_id) values (1, 1);