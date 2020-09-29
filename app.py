from flask import Flask, render_template
from controllers.account_controller import account_blueprint
from controllers.merchants_controller import merchants_blueprint
from controllers.transactions_controller import transactions_blueprint
from controllers.tag_controller import tag_blueprint

app = Flask(__name__)

app.register_blueprint(account_blueprint)
app.register_blueprint(merchants_blueprint)
app.register_blueprint(transactions_blueprint)
app.register_blueprint(tag_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()


# <!-- {% add_transaction_total %}
# {% for  transaction in transactions %}
#     {% amount += transaction.amount %}
#     £{{ amount }}
# {% endfor %} -->
