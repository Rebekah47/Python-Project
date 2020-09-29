from flask import Blueprint, Flask, render_template, request, redirect
from models.account import Account
from models.transaction import Transaction
import repositories.account_repository as account_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository

account_blueprint = Blueprint("account", __name__)
# account home
@account_blueprint.route("/account")
def account():
    accounts = account_repository.select_all_account()
    return render_template("account/account_home.html", accounts=accounts)

@account_blueprint.route("/full_statment", methods=['POST']) 
def check_password():
    password = request.form["password"]
    if password == "hello":
        transactions = transaction_repository.select_all_transactions()
        total_spent = Transaction.add_transaction_total(transactions)
        return render_template("account/full_statment.html", transactions=transactions, total_spent=total_spent)
    else:
        return render_template("account/password_not_a_match.html")

# @account_blueprint.route("/full_statment", methods=['POST'])
# def add_transaction_total():
#     transactions = transaction_repository.select_all_transactions()
#     balance = 0
#     for transaction in transactions:
#         balance += transaction.amount
#     return balance
