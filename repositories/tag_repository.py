from db.run_sql import run_sql
from models.account import Account
from models.merchant import Merchant
from models.transaction import Transaction
from models.tag import Tag
import repositories.account_repository as account_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

def save_tag(tag):
    sql = "INSERT INTO tags (tag_name) VALUES (%s) RETURNING id"
    values = [tag.tag_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id

# SELECT ALL

def select_all_tag():
    tag_selected = []
    sql = 'SELECT * FROM tags'
    results = run_sql(sql)
    for result in results:
        tag = Tag(result['tag_name'], result["id"])
        tag_selected.append(tag)
    return tag_selected

# SELECT
def select_one_tag(id):
    sql = 'SELECT * FROM tags WHERE id = %s'
    values = [id]
    results = run_sql(sql, values)[0]
    tag = Tag(results['tag_name'], results['id'])
    return tag

# DELETE ALL
def delete_all_tags():
    sql = 'DELETE FROM tags'
    run_sql(sql)

# DELETE
def delete_one_tag(id):
    sql = 'DELETE FROM tags WHERE id = %s'
    values = [id]
    run_sql(sql, values)

# UPDATE

def update_account(tag):
    sql = 'UPDATE tags SET (tag_name) = (%s) WHERE id = %s'
    values =  [tag.tag_name, tag.id]
    run_sql(sql, values)