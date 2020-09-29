class Transaction:
    def __init__(self, account, merchant, amount, date, tag, id = None):
        self.account = account
        self.merchant = merchant
        self.amount = amount
        self.date = date
        self.tag = tag
        self.id = id
    
    @classmethod
    def add_transaction_total(cls, transactions):
        total_spent = 0
        for transaction in transactions:
            total_spent += transaction.amount
        return total_spent