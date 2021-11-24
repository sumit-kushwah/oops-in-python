# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
    # this is intializer function not a constructor
    def __init__(self, title):
        self.title = title


# TODO: create instances of the class
b1 = Book('My book title')

# TODO: print the class and property
print(b1)
print(b1.title)
