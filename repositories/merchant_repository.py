from db.run_sql import run_sql
from models.account import Account
from models.merchant import Merchant
from models.transaction import Transaction
from models.tag import Tag
from models.transaction import Transaction
import repositories.account_repository as account_repository
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository

def save_merchant(merchant):
    sql = "INSERT INTO merchants (name, location) VALUES (%s, %s) RETURNING id"
    values = [merchant.name, merchant.location]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id

# SELECT ALL

def select_all_merchants():
    merchants_selected = []
    sql = 'SELECT * FROM merchants'
    results = run_sql(sql)
    for result in results:
        merchant = Merchant(result['name'], result['location'])
        merchants_selected.append(merchant)
    return merchants_selected

# SELECT
def select_one_merchant(id):
    sql = 'SELECT * FROM merchants WHERE id = %s'
    values = [id]
    results = run_sql(sql, values)[0]
    merchant = Merchant(results['name'],results['location'], results['id'])
    return merchant

# DELETE ALL
def delete_all_merchants():
    sql = 'DELETE FROM merchants'
    run_sql(sql)

# DELETE
def delete_one_merchant(id):
    sql = 'DELETE FROM merchants WHERE id = %s'
    values = [id]
    run_sql(sql, values)

# UPDATE

def update_account(merchant):
    sql = 'UPDATE merchants SET (name, location) = (%s, %s) WHERE id = %s'
    values =  [merchant.name, merchant.location, merchant.id]
    run_sql(sql, values)