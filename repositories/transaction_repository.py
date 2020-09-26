from db.run_sql import run_sql
from models.account import Account
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.account_repository as account_repository
import repositories.merchant_repository as merchant_repository

def save_transaction(transaction):
    sql = "INSERT INTO transactions (account_id, merchant_id, amount, date, tag) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [transaction.account_id.id, transaction.merchant_id.id, transaction.amount, transaction.date, transaction.tag]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id

# SELECT ALL
def select_all_transactions():
    transactions = []
    sql = 'SELECT * FROM transactions'
    results = run_sql(sql)
    for result in results:
        account = account_repository.select_one_account(result["account_id"])
        merchant = merchant_repository.select_one_merchant(result["merchant_id"])
        transaction = Transaction(account, merchant, result['amount'], result['date'], result['tag'])
        transactions.append(transaction)
    return transactions

# SELECT

def select_one_transaction(id):
    sql = "SELECT * FROM transaction WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    account = account_repository.select_one_account(result["account_id"])
    merchant = merchant_repository.select_one_merchant(result["merchant_id"])
    transaction = Transaction(account, merchant, result['amount'], result['date'], result['tag'])
    return transaction

# DELETE ALL
def delete_all_transactions():
    sql = "DELETE FROM transactions"
    run_sql(sql)

# DELETE
def delete_one_transaction(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# UPDATE
def update_transaction(transaction):
    sql = "UPDATE transactions SET (account_id, merchant_id, amount, date, tag) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [transaction.account_id.id, transaction.merchant_id.id, transaction.amount, transaction.date, transaction.tag, transaction.id]
    run_sql(sql, values)