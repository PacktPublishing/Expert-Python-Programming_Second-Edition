"""
"Subclassing built-in types" section example of subclassing built-in
dict type.

"""


class DistinctError(ValueError):
    """ Raised when duplicate value is being added to a distinctdict"""


class distinctdict(dict):
    """ Dictionary that does not accept duplicate values"""
    def __setitem__(self, key, value):
        if value in self.values():
            if (
                (key in self and self[key] != value) or
                key not in self
            ):
                raise DistinctError(
                    "This value already exists for different key"
                )

        super().__setitem__(key, value)


if __name__ == "__main__":
    names_to_numbers = {
        "one": 1,
        "two": 2,
        "uno": 1,
    }

    ddict = distinctdict()
    for key, value in names_to_numbers.items():
        try:
            ddict[key] = value
        except DistinctError:
            pass

    print("ordinary dictionary:", names_to_numbers)
    print("distinctdict dictionary:", ddict)
