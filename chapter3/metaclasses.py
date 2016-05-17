"""
"Metaclasses" section example of metaclass that reveal order of all its
methods called.

"""

print(" >>> defining RevealingMeta(type)")


class RevealingMeta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        print(mcs, "__new__ called")
        return super().__new__(mcs, name, bases, namespace)

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print(mcs, "__prepare__ called")
        return super().__prepare__(name, bases, **kwargs)

    def __init__(cls, name, bases, namespace, **kwargs):
        print(cls, "__init__ called")
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        print(cls, "__call__ called")
        return super().__call__(*args, **kwargs)


print(" >>> defining RevealingClass(metaclass=RevealingMeta)")


class RevealingClass(metaclass=RevealingMeta):
    def __new__(cls):
        print(cls, "__new__ called")
        return super().__new__(cls)

    def __init__(self):
        print(self, "__init__ called")
        super().__init__()


if __name__ == "__main__":
    print(" >>> Creating RevealingClass()")
    instance = RevealingClass()
