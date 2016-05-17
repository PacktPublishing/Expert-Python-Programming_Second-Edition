"""
"Decorators" section example of `repeat()` decorator that
preservs decorated function metadata using functools.wraps()

"""
from functools import wraps


def repeat(number=3):
    """Cause decorated function to be repeated a number of times.
    Last value of original function call is returned as a result
    :param number: number of repetitions, 3 if not specified
    """
    def actual_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(number):
                result = function(*args, **kwargs)
            return result
        return wrapper
    return actual_decorator


@repeat(5)
def print_hello_world():
    """ Simplest "hello world" implementation.
    """
    print("Hello, world!")


if __name__ == "__main__":
    print(
        "Result of calling function print_hello_world() "
        "defined with repeat(5) decorator (that preserves "
        "metadata)"
    )
    print_hello_world()
    print()

    print("Name of decorated function:", print_hello_world.__name__)
    print("Docstring of that function:", print_hello_world.__doc__)
