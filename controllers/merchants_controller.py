from flask import Blueprint, Flask, render_template, request, redirect
from models.merchant import Merchant
import repositories.account_repository as account_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository

merchants_blueprint = Blueprint("merchants", __name__)
#transactions home
@merchants_blueprint.route('/merchants')
def merchants():
    merchants = merchant_repository.select_all_merchants()
    return render_template("merchants/merchants_home.html", merchants=merchants)

@merchants_blueprint.route('/add_new_merchant', methods=['POST'])
def add_merchant():
    name = request.form["name"]
    location = request.form["location"]
    merchant = Merchant(name, location)
    merchant_repository.save_merchant(merchant)
    return redirect("/merchants")

# def edit_merchant():
@merchants_blueprint.route("/merchant/<id>/edit")
def edit_merchant(id):
    merchants = merchant_repository.select_all_merchants()
    merchant = merchant_repository.select_one_merchant(id)
    return render_template('merchants/edit_merchants.html', merchant=merchant, merchants=merchants)

@merchants_blueprint.route("/merchants/<id>", methods=["POST"])
def update_merchant(id):
    name = request.form["name"]
    location = request.form["location"]
    edited_merchant = Merchant(name, location, id)
    merchant_repository.update_merchant(edited_merchant)
    return redirect("/merchants")
