# Define the Product class
class Product:
    def __init__(self, price):
        self._price = price  

    # Property to get the price
    @property
    def price(self):
        return self._price

    # Setter to update the price
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Price cannot be negative.")

    # Deleter to delete the price
    @price.deleter
    def price(self):
        print("Price has been deleted.")
        del self._price

# Create a product instance
p = Product(100)

# Print to get the price 
print("Get Price:", p.price)

# Print to update the price
p.price = 150
print("Update Price:", p.price)

# Try setting a negative price
p.price = -20

# Delete the Price
del p.price
