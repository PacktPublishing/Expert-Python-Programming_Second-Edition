"""
"Creational patterns" section example showing different
ways to implement Borg in Python.

"""
class Borg(object):
       _state = {}
       def __new__(cls, *args, **kwargs):
           ob = super().__new__(cls, *args, **kwargs)
           ob.__dict__ = cls._state
           return ob
