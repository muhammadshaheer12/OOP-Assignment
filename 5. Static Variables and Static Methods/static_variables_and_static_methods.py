# Define a class named MathUtils
class MathUtils:
    # Static method to add two numbers
    @staticmethod
    def add(a, b):
        return a + b  

# Call the static method without creating an instance
result = MathUtils.add(10, 5)

# Print the result
print("Sum:", result)
