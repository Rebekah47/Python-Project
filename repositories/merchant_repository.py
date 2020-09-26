from db.run_sql import run_sql
from models.account import Account
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.account_repository as account_repository
import repositories.transaction_repository as transaction_repository

def save_merchant(merchant):
    sql = "INSERT INTO merchants (name, location) VALUES (%s, %s) RETURNING id"
    values = [merchant.name, merchant.location]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id