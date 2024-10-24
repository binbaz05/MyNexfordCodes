# This class defines the products class

class Product:
    def __init__(self, product_id, product_name, product_price, status="Available")
        self.product_id = product_id
        self.product_name = product_name
        self.price = product_price 
        self.status = status

    # create methods for the product class

    def create_product(self):
        print(f"Product {self.product_name} created.")

    def update_product(self, new_name, new_price):
        self.product_name = new_name
        self.product_price = new_price
        print(f"Product {self.product_id} updated to new name {self.product_name} with new price at {self.product_price}")

    def remove_product(self):
        self.status = "Removed"
        print(f"Product {self.product_name} has been removed.")

    
