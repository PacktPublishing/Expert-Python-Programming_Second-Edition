"""
"Properties" section example of writing properties as separate
access methods with class level call to `property()` function.

"""


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    def _width_get(self):
        return self.x2 - self.x1

    def _width_set(self, value):
        self.x2 = self.x1 + value

    def _height_get(self):
        return self.y2 - self.y1

    def _height_set(self, value):
        self.y2 = self.y1 + value

    width = property(
        _width_get, _width_set,
        doc="rectangle width measured from left"
    )
    height = property(
        _height_get, _height_set,
        doc="rectangle height measured from top"
    )

    def __repr__(self):
        return "{}({}, {}, {}, {})".format(
            self.__class__.__name__,
            self.x1, self.y1, self.x2, self.y2
        )


if __name__ == "__main__":
    rectangle = Rectangle(0, 0, 10, 10)
    print(
        "At start we have {} with size of {} x {}"
        "".format(rectangle, rectangle.width, rectangle.height)
    )

    rectangle.width = 2
    rectangle.height = 8
    print(
        "After resizing we have {} with size of {} x {}"
        "".format(rectangle, rectangle.width, rectangle.height)
    )
