# Base class Person
class Person:
    def __init__(self, name):
        self.name = name  

# Derived class Teacher inherits from Person
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)      
        self.subject = subject      

    # Method to display teacher info
    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)

# Create an object of the Teacher class
teacher = Teacher("Sir Ali Aftab Sheikh", "Python")

# Display the teacher's details
teacher.display()
