"""
"Using the __new__() method to override instance creation process" section
example of overriding `__new__()` method when subclassing non-mutable
Python built-in types.

"""


class NonZero(int):
    def __new__(cls, value):
        return super().__new__(cls, value) if value != 0 else None

    def __init__(self, skipped_value):
        # implementation of __init__ could be skipped in this case
        # but it is left to present how it may be not called
        print("__init__() called")
        super().__init__()


if __name__ == "__main__":
    print("NonZero(-12)    =", NonZero(-12))
    print("NonZero(-3.123) =", NonZero(-3.123))
    print("NonZero(0)      =", NonZero(0))

