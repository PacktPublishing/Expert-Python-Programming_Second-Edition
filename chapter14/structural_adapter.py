"""
"Adapters" section example showing how adapters can
be implemented.

"""
from os.path import split, splitext


class DublinCoreAdapter(object):
    def __init__(self, filename):
        self._filename = filename

    @property
    def title(self):
        return splitext(split(self._filename)[-1])[0]

    @property
    def languages(self):
        return 'en',

    def __getitem__(self, item):
        return getattr(self, item, 'Unknown')


class DublinCoreInfo(object):
    def summary(self, dc_dict):
        print('Title: %s' % dc_dict['title'])
        print('Creator: %s' % dc_dict['creator'])
        print('Languages: %s' % ', '.join(dc_dict['languages']))


if __name__ == "__main__":
    file_name = 'example.txt'

    print(
        "Summary of '{}' adapted with DublinCoreAdapter"
        "".format(file_name)
    )
    DublinCoreInfo().summary(DublinCoreAdapter(file_name))
