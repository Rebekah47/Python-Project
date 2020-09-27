from flask import Blueprint, Flask, render_template, request, redirect
from models.tag import Tag
import repositories.account_repository as account_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository

tag_blueprint = Blueprint("tags", __name__)

@tag_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all_tag()
    return render_template("tags/tag_home.html", tags=tags)
