"""
"Using the __new__() method to override instance creation process" section
example of overriding `__new__()` method to count class instances

"""
from random import randint


class InstanceCountingClass:
    instances_created = 0

    def __new__(cls, *args, **kwargs):
        print('__new__() called with:', cls, args, kwargs)
        instance = super().__new__(cls)
        instance.number = cls.instances_created
        cls.instances_created += 1

        return instance

    def __init__(self, attribute):
        print('__init__() called with:', self, attribute)
        self.attribute = attribute


if __name__ == "__main__":
    print(
        "InstanceCountingClass.instances_created =",
        InstanceCountingClass.instances_created
    )

    desired_count = randint(2, 10)
    print(
        "Creating {} instances of InstanceCountingClass..."
        "".format(desired_count)
    )

    for number in range(desired_count):
        InstanceCountingClass(number)

    print(
        "InstanceCountingClass.instances_created =",
        InstanceCountingClass.instances_created
    )
