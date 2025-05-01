# Define the Countdown class
class Countdown:
    def __init__(self, start):
        self.current = start 

    def __iter__(self):
        return self  

    def __next__(self):
        if self.current < 0:
            raise StopIteration 
        value = self.current
        self.current -= 1
        return value

# Create a Countdown object
Countdown = Countdown(5)

# Use the Countdown object in a for-loop
for num in Countdown:
    print(num)
