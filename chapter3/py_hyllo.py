"""
"Hy" section example of importing Hy language modules in Python
as like ordinary Python modules

"""
import hy  # this import statement enables Hy language import hooks

import hyllo


if __name__ == "__main__":
    hyllo.hello()
