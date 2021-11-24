# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, pages, author, price):
        self.title = title
        # TODO: add properties
        self.pages = pages
        self.author = author
        self.price = price
        self.__secret = 'This is secret attribute'
    # TODO: create instance methods

    def setDiscount(self, amount):
        self._discount = amount

    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - self.price * self._discount
        else:
            return self.price


# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: print the price of book1
print(b1.getPrice())


# TODO: try setting the discount
print(b2.getPrice())
b2.setDiscount(0.25)
print(b2.getPrice())

# TODO: properties with double underscores are hidden by the interpreter
print(b2._discount)
print(b2._Book__secret)
