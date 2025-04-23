# Define the decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

# Apply the decorator to a function
@log_function_call
def say_hello():
    print("Hello!")

# Call the decorator function
say_hello()
