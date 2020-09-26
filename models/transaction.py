class Transaction:
    def __init__(self, account_id, merchant_id, amount, date, tag):
        self.account_id = account_id
        self.merchant_id = merchant_id
        self.amount = amount
        self.date = date
        self.tag = tag