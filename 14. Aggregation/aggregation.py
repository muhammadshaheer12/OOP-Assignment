# Define the Employee class
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f"Employee: {self.name}, Position: {self.position}")

# Define the Department class with aggregation
class Department:
    def __init__(self, department_name, employee: Employee):
        self.department_name = department_name
        self.employee = employee 

    def display_department_info(self):
        print(f"Department: {self.department_name}")
        self.employee.display_info() 

employee = Employee("Hamza", "Software Engineer")
department = Department("Computer Engineering", employee)

department.display_department_info() 
