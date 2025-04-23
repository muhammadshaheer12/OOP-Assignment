# Define a class decorator that adds a greet() method
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Apply the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create an object and call the added greet() method
Person = Person("John Doe")
print(Person.greet())
