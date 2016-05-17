"""
"Descriptors" section example of descriptor that allows for lazy
initialization of class instance attributes

"""


class InitOnAccess:
    def __init__(self, klass, *args, **kwargs):
        self.klass = klass
        self.args = args
        self.kwargs = kwargs
        self._initialized = None

    def __get__(self, instance, owner):
        if not self._initialized:
            print('initialized!')
            self._initialized = self.klass(*self.args, **self.kwargs)
        else:
            print('cached!')
        return self._initialized


class MyClass:
    lazily_initialized = InitOnAccess(list, "argument")


if __name__ == "__main__":
    instance = MyClass()

    print("First access to instance.lazily_initialized")
    print(">> instance.lazily_initialized =", instance.lazily_initialized, '\n')

    print("Next access to instance.lazily_initialized")
    print(">> instance.lazily_initialized =", instance.lazily_initialized, '\n')
