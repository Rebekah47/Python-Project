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


# @transactions_blueprint.route('/transactions')
# def transaction_summary():
#     transactions = transaction_repository.select_merchants_transactions(id)
#     render_template("transactions/transactions_summary.html" transactions=transactions)