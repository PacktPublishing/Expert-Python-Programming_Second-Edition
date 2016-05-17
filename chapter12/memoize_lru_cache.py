"""
"Deterministic caching" section example of caching
approach with simple `functools.lrs_cache` decorator.

"""
from functools import lru_cache


@lru_cache(None)
def fibonacci(n):
    """ Return nth Fibonacci sequence number computed recursively
    """
    if n < 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@lru_cache(None)
def two_arg(a, b):
    return a, b

if __name__ == "__main__":
    print([fibonacci(x) for x in range(30)])
    print([two_arg(x, x+1) for x in range(30)])
