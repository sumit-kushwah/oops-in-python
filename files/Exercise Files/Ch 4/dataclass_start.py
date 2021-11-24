# Python Object Oriented Programming by Joe Marini course example
# Using data classes to represent data objects
# This data class introduced in python >= 3.7
from dataclasses import dataclass


@dataclass
class Book:
    class_data = "This is class level data"

    name = "sumit"

    title: str
    author: str
    pages: int
    price: float


# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

# access fields
print(b1.title)
print(b2.author)

# TODO: print the book itself - dataclasses implement __repr__
print(b1)

# TODO: comparing two dataclasses - they implement __eq__
print(b1 == b3)

# TODO: change some fields
b1.pages += 2000

print(b1.pages)
print(b2.pages)
print(b1.class_data)
b1.name = "sumit kushwah"
print(b1.name)
print(b2.name)
print(b2.class_data)
