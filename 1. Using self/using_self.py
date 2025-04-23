# Define a class named Student
class Student:
    # Constructor to initialize name and marks using self
    def __init__(self, name, marks):
        self.name = name    
        self.marks = marks  

    # Method to display the student's details
    def display(self):
        print(f"Student Name: {self.name}")  
        print(f"Marks: {self.marks}")        

# Create an object (instance) of the Student class
student = Student("Ali", 85)

# Call the display method to show the student's details
student.display()
