"""
"Descriptors" section example of descriptor that will allows to
convert a method of a class into lazily evaluated attribute
that will be called only once.

"""


class lazy_class_attribute(object):
    def __init__(self, function):
        self.fget = function

    def __get__(self, obj, cls):
        value = self.fget(obj or cls)
        # note: storing in class object not its instance
        #       no matter if its a class-level or
        #       instance-level access
        setattr(cls, self.fget.__name__, value)
        return value


class MyComplexClass:

    @lazy_class_attribute
    def evaluated_only_once(self):
        print("Evaluation of a method!")
        return sum(x ** 2 for x in range(200))


if __name__ == "__main__":
    instance = MyComplexClass()

    print("First access to attribute at instance level")
    print("instance.evaluated_only_once =",
          instance.evaluated_only_once,
          '\n')

    print("Next access to attribute at instance level")
    print("instance.evaluated_only_once =",
          instance.evaluated_only_once,
          '\n')

    print("Access to attribute at class level")
    print("MyComplexClass.evaluated_only_once =",
          MyComplexClass.evaluated_only_once,
          '\n')

    print("Access to attribute from completely new instance")
    print("MyComplexClass().evaluated_only_once =",
          MyComplexClass().evaluated_only_once,
          '\n')
