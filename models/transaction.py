class Transaction:
    def __init__(self, account, merchant, amount, date, tag, id = None):
        self.account = account
        self.merchant = merchant
        self.amount = amount
        self.date = date
        self.tag = tag
        self.id = id