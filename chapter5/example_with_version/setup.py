"""
"Automated inclusion of version string from package" section example

"""
from setuptools import setup, find_packages
import os


def get_version(version_tuple):
    # additional handling of a,b,rc tags, this can
    # be simpler depending on your versioning scheme
    if not isinstance(version_tuple[-1], int):
        return '.'.join(
            map(str, version_tuple[:-1])
        ) + version_tuple[-1]
    return '.'.join(map(str, version_tuple))

# path to the packages __init__ module in project
# source tree
init = os.path.join(
    os.path.dirname(__file__), 'example_with_version', '__init__.py'
)
version_line = list(
    filter(lambda l: l.startswith('VERSION'), open(init))
)[0]

# VERSION is a tuple so we need to eval its line of code.
# We could simply import it from the package but we
# cannot be sure that this package is importable before
# finishing its installation
VERSION = get_version(eval(version_line.split('=')[-1]))


setup(
    name='example_with_version',
    version=VERSION,
    long_description="""
    Example of automatic inclusion of package version from
    version specifier in package sources
    """,
    packages=find_packages()
)
