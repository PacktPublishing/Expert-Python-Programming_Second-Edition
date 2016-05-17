# Expert Python Programming, Second Edition
 Become an ace Python programmer by learning best coding practices and advance-level concepts with Python 3.5
 
 This is package with code examples for [Python Expert Programming, Second Edition](https://www.packtpub.com/application-development/expert-python-programming-second-edition?utm_source=github&utm_medium=repository&utm_campaign=9781785886850) book.
 
 
## Structure of this package

Content of this package is divided into directories that refer exactly to book chapters. Code may differ sligthly from snippets presented in book. Sometimes it contains additional utilities, functions, or comments, that are intended to improve readability. This should help you better understand topics discussed in the book.

Each chapter directory contains `NOTES` file that explains the order in which scripts should be executed or additional information about its structure.

## How to use this package

In order to use code examples, it is recommended to use virtual environments as explained in Chapter 1, Current Status of Python, of the book.

In short, create new environment somwhere on you disk. Make sure you are using at least Python 3.5 version to create virtual environment

    $ python3.5 -m venv book-env

Book also covers topic of compatibility issues between Python 2 and Python 3 in certain sections. If you want to run scripts in older versions of Python, use `virtualenv` tool to create additional environment on your disk. Make sure to name it differently, so it will be clear which environment you are using in given shell session:

    $ virtualenv -p python2.7 book-py27-env

If your environment is already created, you are ready to activate it so all installed packages will be isolated from your base system Python environment. If you are using bash, execute the following line:

    $ source book-env/bin/activate

If you are working in Windows command line or Power Shell, then type:

    > book-env\Scripts\activate

Successful activation will change your shell prompt by adding environment name prefix:

    (book-env)$

Now, you can finally use `pip` to install all packages that are mentioned in book and used in example scripts:

    (book-env)$ pip install -r requirements.txt


## Want to learn more on Python?
* [Python Machine Learning](https://www.packtpub.com/big-data-and-business-intelligence/python-machine-learning?utm_source=github&utm_medium=repository&utm_campaign=9781785886850)
* [Mastering Object-oriented Python](https://www.packtpub.com/application-development/mastering-object-oriented-python?utm_source=github&utm_medium=repository&utm_campaign=9781785886850)
* [Mastering Python](https://www.packtpub.com/application-development/mastering-python?utm_source=github&utm_medium=repository&utm_campaign=9781785886850)
