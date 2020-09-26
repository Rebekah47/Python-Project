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