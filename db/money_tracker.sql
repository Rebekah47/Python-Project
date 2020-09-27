DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS tags;

CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(255),
    balance FLOAT, 
    transaction_summary TEXT 
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255)
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    tag_name VARCHAR(255)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    account_id INT REFERENCES accounts(id),
    merchant_id INT REFERENCES merchants(id),
    tag_id INT REFERENCES tags(id),
    amount FLOAT,
    date VARCHAR(255)
);