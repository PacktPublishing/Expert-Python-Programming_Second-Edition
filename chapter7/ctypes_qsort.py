# -*- coding: utf-8 -*-
from random import shuffle

import ctypes
from ctypes.util import find_library

libc = ctypes.cdll.LoadLibrary(find_library('c'))

CMPFUNC = ctypes.CFUNCTYPE(
    # return type
    ctypes.c_int,
    # first argument type
    ctypes.POINTER(ctypes.c_int),
    # second argument type
    ctypes.POINTER(ctypes.c_int),
)


def ctypes_int_compare(a, b):
    # arguments are pointers so we access using [0] index
    print(" %s cmp %s" % (a[0], b[0]))

    # according to qsort specification this should return:
    # * less than zero if a < b
    # * zero if a == b
    # * more than zero if a > b
    return a[0] - b[0]


def main():
    numbers = list(range(5))
    shuffle(numbers)
    print("shuffled: ", numbers)

    # create new type representing array with lenght
    # same as the lenght of numbers list
    NumbersArray = ctypes.c_int * len(numbers)
    # create new C array using a new type
    c_array = NumbersArray(*numbers)

    libc.qsort(
        # pointer to the sorted array
        c_array,
        # length of the array
        len(c_array),
        # size of single array element
        ctypes.sizeof(ctypes.c_int),
        # callback (pointer to the C comparison function)
        CMPFUNC(ctypes_int_compare)
    )
    print("sorted:   ", list(c_array))


if __name__ == "__main__":
    main()
