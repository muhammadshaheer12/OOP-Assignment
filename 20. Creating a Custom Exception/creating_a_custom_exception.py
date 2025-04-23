# Define a custom exception class
class InvalidAgeError(Exception):
    pass  

# Function to check age and raise custom exception if needed
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    else:
        print("Access granted.")

# Try...except block to handle the custom exception
try:
    user_age = 16 
    check_age(user_age)
except InvalidAgeError as e:
    print("InvalidAgeError:", e)
