class Transaction:
    def __init__(self, account_id, merchant_id, amount, date, tag_id, id = None):
        self.account_id = account_id
        self.merchant_id = merchant_id
        self.amount = amount
        self.date = date
        self.tag_id = tag_id
        self.id = id