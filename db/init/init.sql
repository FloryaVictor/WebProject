
-- init tables
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email varchar(64) NOT NULL UNIQUE,
    name varchar(64) NOT NULL,
    password varchar(64) NOT NULL,
    phone_number varchar(20) NOT NULL UNIQUE,
    role text DEFAULT 'customer' NOT NULL, 
    address text NOT NULL,
    balance real DEFAULT 0.0 NOT NULL,
    CHECK (balance >= 0.0)
);

CREATE TABLE delivery (
    id SERIAL PRIMARY KEY,
    name varchar(64) NOT NULL,
    price real DEFAULT 0.0 NOT NULL, 
    rating real,
    CHECK (price >= 0.0), 
    CHECK (rating >= 0.0 AND rating <= 10.0)
);

CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    name varchar(64) NOT NULL,
    description text, 
    price real DEFAULT 0.0 NOT NULL, 
    photo_url text,
    CHECK (price >= 0.0)
);

CREATE TABLE restaurant (
    id SERIAL PRIMARY KEY,
    name varchar(64) NOT NULL, 
    address text NOT NULL,
    rating real, 
    description text,
    CHECK (rating >= 0.0 AND rating <= 10.0)
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    price real DEFAULT 0.0 NOT NULL,
    date date NOT NULL DEFAULT current_date,
    customer_id integer REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE,
    restaurant_id integer REFERENCES restaurant(id) ON UPDATE CASCADE ON DELETE CASCADE,
    delivery_id integer REFERENCES delivery(id) ON UPDATE CASCADE ON DELETE CASCADE,
    CHECK (price >= 0.0)
);


CREATE TABLE order_product (
    order_id integer REFERENCES orders(id) ON UPDATE CASCADE ON DELETE CASCADE,
    product_id integer REFERENCES product(id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE restaurant_delivery (
    restaurant_id  integer REFERENCES restaurant(id) ON UPDATE CASCADE ON DELETE CASCADE,
    delivery_id integer REFERENCES delivery(id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE restaurant_product (
    restaurant_id  integer REFERENCES restaurant(id) ON UPDATE CASCADE ON DELETE CASCADE,
    product_id integer REFERENCES product(id) ON UPDATE CASCADE ON DELETE CASCADE
);


-- some dummy entries
INSERT INTO users(email, name, password, phone_number, address) VALUES 
    ('pupkin@mail.ru', 'vasya', 'strong pass', '88005553535', 'улица Пушнкина, 4'),
    ('sergeich@gmail.com', 'sergey', 'ochen strong pass', '89231721754', 'Омск');

INSERT INTO restaurant(name, address, rating, description) VALUES 
    ('Moscow burger', 'а где мы?', 0.0, 'не вкусно'),
    ('Omsk dishes', 'а мы повсюду', 10.0, '10/10');

INSERT INTO delivery(name, price, rating) VALUES 
    ('BistroNog', 135, 7.0),
    ('WindWings', 150, 10.0);

INSERT INTO product(name, description, price) VALUES 
    ('Apple', 'regular apple', 2.5),
    ('Steak', 'meat', 23.99);


--------------------------------
-- CREATE TABLE customer (
--     id SERIAL PRIMARY KEY,
--     first_name varchar(40) NOT NULL,
--     last_name varchar(40) NOT NULL,
--     email varchar(256) NOT NULL UNIQUE,
--     password varchar(256) NOT NULL,
--     phone varchar(10),
--     address text,
--     registration_date date DEFAULT CURRENT_DATE
-- );

-- CREATE TABLE preferences(
--     customer_id integer REFERENCES customer(id) ON DELETE CASCADE ON UPDATE CASCADE,
--     advertising boolean DEFAULT TRUE
-- );

-- CREATE TABLE product(
--     id SERIAL PRIMARY KEY,
--     name text NOT NULL,
--     price money DEFAULT 0.0
-- );

-- CREATE TABLE product_meta(
--     product_id integer REFERENCES product(id) ON DELETE CASCADE ON UPDATE CASCADE,
--     category text,
--     tags text[]
-- );


-- CREATE TABLE orders(
--     id SERIAL PRIMARY KEY,
--     customer_id integer REFERENCES customer(id) ON DELETE RESTRICT ON UPDATE CASCADE,
--     order_date date DEFAULT CURRENT_DATE,
--     total money DEFAULT 0.0
-- );

-- CREATE TABLE order_product(
--     order_id integer REFERENCES orders(id) ON UPDATE CASCADE,
--     product_id integer REFERENCES product(id) ON UPDATE CASCADE,
--     price money,
--     quantity integer DEFAULT 0
-- );

-- CREATE OR REPLACE FUNCTION op_audit() RETURNS TRIGGER AS $op_audit$
--     BEGIN
--         IF (TG_OP = 'INSERT') THEN
--             IF (NEW.price is NULL) THEN
--                 NEW.price = price FROM product WHERE id = NEW.product_id;
--             END IF;
--             UPDATE orders SET total = total + NEW.price * NEW.quantity;
--             RETURN NEW;
--         ELSIF (TG_OP = 'UPDATE') THEN
--             UPDATE orders SET total = total - OLD.price * OLD.quantity;
--             UPDATE orders SET total = total + NEW.price * NEW.quantity;
--             return NEW;
--         ELSIF (TG_OP = 'DELETE') THEN
--             UPDATE orders SET total = total - OLD.price * OLD.quantity;
--             RETURN OLD;
--         END IF;

--     END;
-- $op_audit$ LANGUAGE plpgsql;

-- CREATE TRIGGER op_audit
--     BEFORE INSERT OR UPDATE OR DELETE ON order_product
--         FOR EACH ROW EXECUTE PROCEDURE op_audit();

-- --
-- INSERT INTO customer(first_name, last_name, email, password, phone, address) VALUES ('Jhon', 'Goodson', 'jg@gmail.com', 'whhhwrtht', 8213254512, 'LA');
-- INSERT INTO product(name, price) values ('apple', 0.75);
-- INSERT INTO orders(customer_id) values (1);
-- INSERT INTO order_product(order_id, product_id, quantity) values(1, 1, 2);
