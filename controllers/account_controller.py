from flask import Blueprint, Flask, render_template, request, redirect
from models.account import Account
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