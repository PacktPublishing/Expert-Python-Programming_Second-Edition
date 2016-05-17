"""
"Descriptors" section example of descriptor that will reveal its
 access by printing information on stdout.

"""


class RevealAccess(object):
    """
    A data descriptor that sets and returns values
    normally and prints a message logging their access.
    """
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val


class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5


if __name__ == "__main__":
    my_instance = MyClass()

    # set x attribute (will issue print)
    my_instance.x = 4
    # access x attribute (will issue print)
    assert my_instance.x == 4

    # set y attribute (will pass silently)
    my_instance.y = 2
    # access x attribute (will pass silently)
    assert my_instance.y == 2
