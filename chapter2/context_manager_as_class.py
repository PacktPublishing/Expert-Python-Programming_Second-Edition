"""
"Context managers - the with statement" section example of
context manager implemented as a class

"""


class ContextIllustration:
    def __enter__(self):
        print('* entering context')

    def __exit__(self, exc_type, exc_value, traceback):
        print('* leaving context')
        if exc_type is None:
            print('* with no error')
        else:
            print('* with an error (%s)' % exc_value)


if __name__ == "__main__":
    print("Process of running code within context manager WITHOUT error")

    with ContextIllustration():
        print(">> inside context")
    print()

    print("Process of running code within context manager WITH error")
    try:
        with ContextIllustration():
            print(">> inside context")
            raise RuntimeError("Exception inside context manager")
    except RuntimeError:
        pass
