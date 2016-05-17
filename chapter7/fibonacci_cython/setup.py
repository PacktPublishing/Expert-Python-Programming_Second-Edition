from setuptools import setup
from Cython.Build import cythonize


setup(
    name='fibonacci',
    ext_modules=cythonize(['fibonacci.pyx'])
)
