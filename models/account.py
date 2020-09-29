class Account:
    def __init__(self, user_name, balance, transaction_summary = [], id = None):
        self.user_name = user_name
        self.balance = balance
        self. transaction_summary = transaction_summary
        self.id = id

    # def change_login(self):
    #     if self.login == True:
    #         self.login = False
    #     else:
    #         self.login = True
    
    def update_balance(self, transaction_total):
        self.balance -= transaction_total

# database table
# change repository/s
# controller password 