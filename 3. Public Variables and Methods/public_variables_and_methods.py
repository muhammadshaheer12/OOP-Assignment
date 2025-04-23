# Define a class named Car
class Car:
    # Public variable (accessible from outside the class)
    brand = "Toyota"

    # Public method (accessible from outside the class)
    def start(self):
        print(f"The {self.brand} car is starting...")

# Create an object of the Car class
my_car = Car()

# Access the public variable directly
print("Car Brand:", my_car.brand)

# Call the public method
my_car.start()
