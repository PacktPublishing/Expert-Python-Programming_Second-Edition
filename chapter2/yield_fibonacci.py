"""
"The yield statement" section example of fibonacci generator

"""


def fibonacci():
    a, b = 0, 1

    while True:
        yield b
        a, b = b, a + b


if __name__:
    fib = fibonacci()

    print("Return type of fibonacci function:", type(fib))
    print(
        "First 10 fibonacci numbers (using next):",
        [next(fib) for _ in range(10)]
    )
    print(
        "Next 10 fibonacci numbers (continued):",
        [next(fib) for _ in range(10)]
    )

