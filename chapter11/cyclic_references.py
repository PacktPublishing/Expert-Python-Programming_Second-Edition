"""
"Profiling memory" section example of how CPython
deals with cyclic references in different versions
of interpreter.

"""
import gc
import platform

import objgraph


class WithDel(list):
    """ list subclass with custom __del__ implementation """
    def __del__(self):
        pass


def main():
    x = WithDel()
    y = []
    z = []

    x.append(y)
    y.append(z)
    z.append(x)

    del x, y, z

    print("unreachable prior collection: %s" % gc.collect())
    print("unreachable after collection: %s" % len(gc.garbage))
    print("WithDel objects count:        %s" % objgraph.count('WithDel'))


if __name__ == "__main__":
    print("Python version: %s" % platform.python_version())
    print()
    main()
