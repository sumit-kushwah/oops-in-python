# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces

from abc import ABC, abstractmethod


class JSONinfy(ABC):
    @abstractmethod
    def toJSON():
        pass


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape, JSONinfy):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        return "{{\"Circle\" : {}}}".format(self.calcArea())


c = Circle(10)
print(c.calcArea())
print(c.toJSON())
