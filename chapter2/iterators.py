"""
"Iterators" section example of a sinple count down iterator

"""
from time import sleep


class CountDown:
    def __init__(self, step):
        self.step = step

    def __next__(self):
        """Return the next element."""
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        """Return the iterator itself."""
        return self


if __name__ == "__main__":
    print("Counting down:")

    for element in CountDown(10):
        print('*', element)
        sleep(0.2)
