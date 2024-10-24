# Import all classes for the Policy Management System for an Insurance Company

from PolicyHolders import Policyholder
from Products import Product
from Payments import Payment

if __name__ == "__main__":

    # initiate a product 

    product1 = Product(101, "Group Life", 400)
    product2 = Product(201, "Pet Insurance", 50)
    print("\n")
    print("-" * 40)

    # create product

    product1.create_product()
    product2.create_product()
    print("\n")
    print("-" * 40)

    # initiate a policyholder
    policyholder1 = Policyholder(1, "Hassan Abbas", "binbaz0t#gmail.com")
    policyholder2 = Policyholder(2, "Alson Lee", "Alsonlee@gmail.com")

    policyholder1.register_policyholder()
    policyholder2.register_policyholder()
    print("\n")
    print("-" * 40)

    # Add Policies to Policyholders Record
    policyholder1.add_policy(product1)
    policyholder2.add_policy(product2)
    print("\n")
    print("-" * 40)

    # Process Payments

    payment1 = Payment(1, product1.product_name, product1.product_price)
    payment2 = Payment(2, product2.product_name, product2.product_price)

    policyholder1.add_payment(payment1)
    policyholder2.add_payment(payment2)

    payment1.process_payment()
    payment2.process_payment()
    print("\n")
    print("-" * 40)

    # Suspend and reactivate a Policyholder
    policyholder1.suspend_policyholder()
    policyholder1.reactivate_policyholder()
    print("\n")
    print("-" * 40)

    # Show Policyholder details
    policyholder1.show_details()
    print("\n")
    print("-" * 40)
    policyholder2.show_details()
    print("\n")



