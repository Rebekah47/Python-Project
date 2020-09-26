from db.run_sql import run_sql
from models.account import Account
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

def save_account(account):
    sql = "INSERT INTO accounts (user_name, balance, transaction_summary) VALUES (%s, %s, %s) RETURNING id"
    values = [account.user_name, account.balance, account.transaction_summary]
    results = run_sql(sql, values)
    id = results[0]['id']
    account.id = id

# SELECT ALL

def select_all_account():
    accounts_selected = []
    sql = 'SELECT * FROM accounts'
    results = run_sql(sql)
    for result in results:
        account = Account(result['user_name'], result['balance'], result['transaction_summary'], result['id'])
        accounts_selected.append(account)
    return accounts_selected

# SELECT
def select_one_account(id):
    sql = 'SELECT * FROM accounts WHERE id = %s'
    values = [id]
    results = run_sql(sql, values)[0]
    account = Account(results['user_name'],results['balance'], results['transaction_summary'], results['id'])
    return account

# DELETE ALL
def delete_all_accounts():
    sql = 'DELETE FROM accounts'
    run_sql(sql)

# DELETE
def delete_one_account(id):
    sql = 'DELETE FROM accounts WHERE id = %s'
    values = [id]
    run_sql(sql, values)

# UPDATE

def update_account(account):
    sql = 'UPDATE accounts SET (user_name, balance, transaction_summary) = (%s, %s, %s) WHERE id = %s'
    values = [account.user_name, account.balance, account.transaction_summary, account.id]
    run_sql(sql, values)