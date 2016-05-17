"""
"README file" section example presenting how to convert READMEs
from various markups to reStructuredText using pypandoc.

"""
from setuptools import setup, find_packages
import os


try:
    from pypandoc import convert

    def read_md(f):
        return convert(f, 'rst')

except ImportError:
    convert = None
    print(
        "warning: pypandoc module not found, could not convert Markdown to RST"
    )

    def read_md(f):
        return open(f, 'r').read()

README = os.path.join(os.path.dirname(__file__), 'README.md')

setup(
    name='example_with_readme_conversion',
    long_description=read_md(README),
    packages=find_packages()
)
