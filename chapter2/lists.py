"""
"List and tuples" section examples of list comprehension usage

"""


def evens_using_for_loop(count):
    """ Calculate evens using for loop """
    evens = []
    for i in range(count):
        if i % 2 == 0:
            evens.append(i)
    return evens


def evens_using_list_comprehension(count):
    """ Calculate evens using list comprehension """
    return [i for i in range(count) if i % 2 == 0]


def enumerate_elements(elements):
    for index, element in enumerate(elements):
        print(index, element)


if __name__ == "__main__":
    print(
        "0-10 evens calculated in for loop:",
        evens_using_for_loop(11)
    )
    print()

    print(
        "0-10 evens calculated in list comprehension:",
        evens_using_list_comprehension(11)
    )
    print()

    print("0-10 evens enumerated:")
    enumerate_elements(evens_using_list_comprehension(11))
    print()

