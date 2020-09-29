from db.run_sql import run_sql
from models.account import Account
from models.merchant import Merchant
from models.transaction import Transaction
from models.tag import Tag
import repositories.account_repository as account_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

def save_transaction(transaction):
    sql = "INSERT INTO transactions (account_id, merchant_id, amount, date, tag_id) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [transaction.account.id, transaction.merchant.id, transaction.amount, transaction.date, transaction.tag.id]
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
        tag = tag_repository.select_one_tag(result["tag_id"])
        transaction = Transaction(account, merchant, result['amount'], result['date'], tag, result['id'])
        transactions.append(transaction)
    return transactions

# SELECT

def select_one_transaction(id):
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    account = account_repository.select_one_account(result["account_id"])
    merchant = merchant_repository.select_one_merchant(result["merchant_id"])
    tag = tag_repository.select_one_tag(result["tag_id"])
    transaction = Transaction(account, merchant, result['amount'], result['date'], tag, result['id'])
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
    print(transaction.amount)
    sql = "UPDATE transactions SET (account_id, merchant_id, amount, date, tag_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [transaction.account.id, transaction.merchant.id, transaction.amount, transaction.date, transaction.tag.id, transaction.id]
    run_sql(sql, values)

    # Select transactions with merchants
# def select_merchants_transactions(id):
#     sql = "SELECT merchants.name, merchants.location FROM merchants INNER JOIN transactions ON transactions.merchant_id = merchants.id"
#     values = [id]
#     results = run_sql(sql, values)
#     for row in results:
#         summary = Account(row['user_name'], row['balance'], row['transaction_summary'])
#     return summary
