# -*- coding: utf-8 -*-
import ctypes
from ctypes.util import find_library

libc = ctypes.cdll.LoadLibrary(find_library('c'))


if __name__ == "__main__":
    libc.printf(b"Hello world!\n")
