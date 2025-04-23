# Define a class named Logger
class Logger:
    # Constructor: called when an object is created
    def __init__(self):
        print("Logger initialized: Object created.")

    # Destructor: called when an object is destroyed
    def __del__(self):
        print("Logger terminated: Object destroyed.")

# Create an object of the Logger class
log = Logger()
