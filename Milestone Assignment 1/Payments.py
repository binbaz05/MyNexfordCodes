from datetime import datetime

# create payment class

class Payment:
    def __init__(self, payment_id, product_name, amount, payment_date=None, penalty=0):
        self.payment_id = payment_id
        self.product_name = product_name
        self.amount = amount
        self.payment_date = payment_date or datetime.now()
        self.penalty = penalty

    # create payments methods

    def process_payment(self):
        print(f"Payment of {self.amount} processed for  {self.product_name}.")

    def apply_penalty(self, penalty_amount):
        self.penalty = penalty_amount
        print(f"Penalty of {self.penalty} applied to {self.product_name}.")

    
