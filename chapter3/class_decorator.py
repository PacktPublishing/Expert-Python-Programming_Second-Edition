"""
"Class decorators" section example of simple usage of decorators
in context of classes (with monkey patching)
"""


def short_repr(cls):
    cls.__repr__ = lambda self: super(cls, self).__repr__()[:8]
    return cls


@short_repr
class ClassWithRelativelyLongName:
    pass


if __name__ == "__main__":
    print("Class real name:", ClassWithRelativelyLongName.__name__)
    print("Instance representation (decorated):", ClassWithRelativelyLongName())
