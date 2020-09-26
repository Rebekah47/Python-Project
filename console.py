import pdb

from models.account import Account
import repositories.account_repository as account_repository

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository

account_1 = Account("Account", 450.60)
account_repository.save_account(account_1)

merchant_1 = Merchant("Morrisons", "Edinburgh")
merchant_repository.save_merchant(merchant_1)
merchant_2 = Merchant("Scotrail", "Glasgow")
merchant_repository.save_merchant(merchant_2)
merchant_3 = Merchant("PINK", "Glasgow")
merchant_repository.save_merchant(merchant_3)

transaction_1 = Transaction(account_1, merchant_1, 14.95, "25/01/2020", "groceries")
transaction_repository.save_transaction(transaction_1)
transaction_2 = Transaction(account_1, merchant_2, 22.50, "27,01,2020", 'travel')
transaction_repository.save_transaction(transaction_2)
transaction_3 = Transaction(account_1, merchant_3, 120, "30/01/2020", "clothes")
transaction_repository.save_transaction(transaction_3)

pdb.set_trace()