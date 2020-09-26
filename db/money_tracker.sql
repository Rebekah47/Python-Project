DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS merchants;

CREATE TABLE accounts(
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(255),
    balance INT, 
    transaction_summary TEXT 
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    account_id INT REFERENCES accounts(id),
    merchant_id INT REFERENCES merchant(id),
    amount INT,
    date VARCHAR(255), 
    tag TAG
)