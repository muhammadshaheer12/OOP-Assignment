# Define a class named Book
class Book:
    # Class variable to keep track of total books
    total_books = 0

    def __init__(self, title):
        self.title = title
        # Increment the total_books count using the class method
        Book.increment_book_count()

    # Class method to increment total_books
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Create some book objects
book1 = Book("Python Basics")
book2 = Book("Data Science Essentials")
book3 = Book("Machine Learning 101")

# Print the total number of books
print("Total books:", Book.total_books)
