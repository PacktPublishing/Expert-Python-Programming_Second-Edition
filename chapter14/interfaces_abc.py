"""
"Interfaces" section example showing how implicit interfaces
can be created and verified using Abstract Base Classes.

"""
from abc import (
    ABCMeta,
    abstractmethod,
    abstractproperty
)


class IRectangle(metaclass=ABCMeta):

    @abstractproperty
    def width(self):
        return

    @abstractproperty
    def height(self):
        return

    @abstractmethod
    def area(self):
        """ Return rectangle area
        """

    @abstractmethod
    def perimeter(self):
        """ Return rectangle perimeter
        """

    @classmethod
    def __subclasshook__(cls, C):
        if cls is IRectangle:
            if all([
                any("area" in B.__dict__ for B in C.__mro__),
                any("perimeter" in B.__dict__ for B in C.__mro__),
                any("width" in B.__dict__ for B in C.__mro__),
                any("height" in B.__dict__ for B in C.__mro__),
            ]):
                return True
        return NotImplemented


class Rectangle(IRectangle):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2


class ImplicitRectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2


if __name__ == "__main__":
    rectangle = Rectangle(10, 10)

    print("Instance type:", type(rectangle))
    print("Instance MRO: ", rectangle.__class__.mro())
    print("isinstance(rectangle, IRectangle) =",
          isinstance(rectangle, IRectangle))
    print()

    rectangle = ImplicitRectangle(10, 10)
    print("Instance type:", type(rectangle))
    print("Instance MRO: ", rectangle.__class__.mro())
    print("isinstance(rectangle, IRectangle) =",
          isinstance(rectangle, IRectangle))
    print()
