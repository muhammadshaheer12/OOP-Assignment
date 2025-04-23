# Define a class named Multiplier
class Multiplier:
    # Constructor to initialize the Multiplier factor
    def __init__(self, factor):
        self.factor = factor  
    # __call__ method allows the object to be called like a function
    def __call__(self, value):
        return value * self.factor  

# Create an instance of the Multiplier class with a factor of 5
m = Multiplier(5)

# Check if the object 'm' is callable
print("Is 'm' callable?", callable(m))

# Call the object like a function with value 10
result = m(10)

# Print the result of the Multiplier
print("Result of m(10):", result)
