# Define a class named Bank
class Bank:
    # Class variable shared by all instances
    bank_name = "HBL"  

    # Class method to change the bank name using cls
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  

    # Method to display the current bank name
    def show_bank(self):
        print(f"Bank Name: {self.bank_name}")

# Create instances of Bank
customer1 = Bank()
customer2 = Bank()

# Show bank name before change
print("Before changing bank name:")
customer1.show_bank()
customer2.show_bank()

# Change the bank name using the class method
Bank.change_bank_name("UBL")  

# Show bank name after change
print("\nAfter changing bank name:")
customer1.show_bank()
customer2.show_bank()
