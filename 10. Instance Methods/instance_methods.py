# Define a class named Dog
class Dog:
    # Constructor to initialize instance variables
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed 

    # Instance method to print a message including the dog's name
    def bark(self):
        print(f"{self.name} says Bark!")

# Create an object of the Dog class
dog = Dog("Sable", "Golden Retriever")

# Call the bark method
dog.bark()
