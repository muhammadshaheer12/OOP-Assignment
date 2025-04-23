# Define a class named Counter
class Counter:
    # Class variable to keep track of the number of objects created
    count = 0

    # Constructor that increments the count whenever a new object is created
    def __init__(self):
        Counter.count += 1  

    # Class method to access and display the count using 'cls'
    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")  

# Create some objects of the Counter class
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Call the class method to display the count
Counter.display_count()
