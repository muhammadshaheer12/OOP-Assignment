from abc import ABC, abstractmethod

# Define an abstract base class named Shape
class Shape(ABC):
    # Abstract method (must be implemented by subclasses)
    @abstractmethod
    def area(self):
        pass

# Subclass Rectangle inherits from Shape and implements area()
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implement the abstract method
    def area(self):
        return self.width * self.height

# Create an object of Rectangle and call the area method
rect = Rectangle(5, 3)
print("Area of Rectangle:", rect.area())
