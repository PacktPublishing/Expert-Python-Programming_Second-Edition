"""
"The yield statement" section example of chaining multiple generators

"""


def power(values):
    for value in values:
        print('powering %s' % value)
        yield value ** 2


def adder(values):
    for value in values:
        print('adding to %s' % value)
        if value % 2 == 0:
            yield value + 3
        else:
            yield value + 2


if __name__ == "__main__":
    elements = list(range(5))

    print(
        "Processing list of {} elements in form of adder(power(elements))"
        "".format(elements)
    )
    print("Result =", list(adder(power(elements))))
    print()

    print(
        "Processing list of {} elements in form of power(adder(elements))"
        "".format(elements)
    )
    print("Result =", list(power(adder(elements))))
    print()
