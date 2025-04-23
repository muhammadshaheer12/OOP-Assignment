# Define a class named Employee
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         
        self._salary = salary    
        self.__ssn = ssn         

# Create an object of the Employee class
emp = Employee("shaheer", 50000, "123-45-6789")

# Try accessing the public variable
print("Public - Name:", emp.name)  

# Try accessing the protected variable
print("Protected - Salary:", emp._salary)  

# Try accessing the private variable
try:
    print("Private - SSN:", emp.__ssn)  
except AttributeError:
    print("Private - SSN: Cannot access directly (AttributeError)")

# Accessing private variable using name mangling
print("Private - SSN (via name mangling):", emp._Employee__ssn)
