"""
"Context managers - the with statement" section example of
context manager implemented as a function

"""
from contextlib import contextmanager


@contextmanager
def context_illustration():
    print('entering context')
    try:
        yield
    except Exception as e:
        print('leaving context')
        print('with an error (%s)' % e)
        # exception needs to be reraised
        raise
    else:
        print('leaving context')
        print('with no error')


if __name__ == "__main__":
    print("Process of running code within context manager WITHOUT error")

    with context_illustration():
        print(">> inside context")
    print()

    print("Process of running code within context manager WITH error")
    try:
        with context_illustration():
            print(">> inside context")
            raise RuntimeError("Exception inside context manager")
    except RuntimeError:
        pass
