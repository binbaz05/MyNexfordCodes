from datetime import datetime

# create policyholder class

class Policyholder:
    def __init__(self, policyholder_id, name, email, status = "Active"):
        self.policyholder_id = policyholder_id
        self.name = name
        self.email =  email
        self.status = status
        self.policies = []
        self.payments = []


    # Create policyholder class methods

    def register_policyholder(self):
        print(f"Policyholder {self.name} has been registered.")

    def suspend_policyholder(self):
        self.status = "Suspended"
        print(f"Policyholder {self.name} has been suspended.")
    
    def reactivate_policyholder(self):
        self.status = "Active"
        print(f"Policyholder {self.name} has been reactivated.")

    def add_policy(self, policy):
        self.policies.append(policy)
        print(f"Policy {policy.product_name} added to {self.name}'s account.")

    def add_payment(self, payment):
        self.payments.append(payment)
        print(f"Payment of {payment.amount} for {payment.product_name} added for {self.name}.")
    
    def show_details(self):
        print(f"\nPolicyholder: {self.name}")
        print(f"Email: {self.email}")
        print(f"Status: {self.status}")
        print(f"Policies: {[policy.product_name for policy in self.policies]}")
        print(f"Payments: {[f'{payment.amount} for {payment.product_name}' for payment in self.payments]}")
        

