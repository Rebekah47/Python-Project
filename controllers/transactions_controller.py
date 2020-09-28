from flask import Blueprint, Flask, render_template, request, redirect
from models.transaction import Transaction
import repositories.account_repository as account_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route('/transactions')
def transactions():
    transactions = transaction_repository.select_all_transactions()
    return render_template('transactions/transactions_summary.html', transactions=transactions)

@transactions_blueprint.route('/add_new_transaction')
def add_transaction():
    accounts = account_repository.select_all_account()
    merchants = merchant_repository.select_all_merchants()
    tags = tag_repository.select_all_tag()
    return render_template('transactions/new_transaction.html', accounts=accounts, merchants=merchants, tags=tags)

@transactions_blueprint.route('/add_new_transaction', methods=['POST'])
def create_transaction():
    account_id = request.form["account_name"]
    account = account_repository.select_one_account(account_id)
    merchant_id = request.form["merchant_name"]
    merchant = merchant_repository.select_one_merchant(merchant_id)
    amount = request.form["amount"]
    date = request.form["date"]
    tag_id = request.form["tag"]
    tag = tag_repository.select_one_tag(tag_id)
    new_transaction = Transaction(account, merchant, amount, date, tag)
    transaction_repository.save_transaction(new_transaction)
    return redirect('/transactions')

@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    print(id)
    transaction_repository.delete_one_transaction(id)
    return redirect('/transactions')

@transactions_blueprint.route("/transactions/<id>/edit", methods=['POST'])
def edit_transaction(id):
    transaction = transaction_repository.select_one_transaction(id)
    accounts = account_repository.select_all_account()
    merchants = merchant_repository.select_all_merchants()
    tags = tag_repository.select_all_tag()
    return render_template('transactions/edit_transaction.html', transaction=transaction, accounts=accounts, merchants=merchants, tags=tags)

# @transactions_blueprint.route("/transactions/<id>/edit", methods=['POST'])
# def update_transaction():
#     account_id = request.form["account_name"]
#     account = account_repository.select_one_account(account_id)
#     merchant_id = request.form["merchant_name"]
#     merchant = merchant_repository.select_one_merchant(merchant_id)
#     amount = request.form["amount"]
#     date = request.form["date"]
#     tag_id = request.form["tag"]
#     tag = tag_repository.select_one_tag(tag_id)
#     edited_transaction = Transaction(account, merchant, amount, date, tag)
#     transaction_repository.save_transaction(edited_transaction)
#     return redirect('/transactions')




# @transactions_blueprint.route('/transactions')
# def transaction_summary():
#     transactions = transaction_repository.select_merchants_transactions(id)
#     render_template("transactions/transactions_summary.html" transactions=transactions)