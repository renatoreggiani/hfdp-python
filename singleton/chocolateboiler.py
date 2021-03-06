"""
Chocolate boiler with thread-safe singleton

Author: m1ge7
Date: 2014/03/27
"""

import thread


class ChocolateBoiler(object):
    _instance = None
    _lock = thread.allocate_lock()

    def __new__(cls):
        cls._lock.acquire()
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        cls._lock.release()
        return cls._instance

    def __init__(self):
        self._empty = True
        self._boiled = False

    def fill(self):
        if self.is_empty():
            self._empty = False
            self._boiled = False

    def drain(self):
        if not self.is_empty() and self.is_boiled():
            self._empty = True

    def boil(self):
        if not self.is_empty() and self.is_boiled():
            self._boiled = True

    def is_empty(self):
        return self._empty

    def is_boiled(self):
        return self._boiled


if __name__ == '__main__':
    boiler = ChocolateBoiler()
    boiler.fill()
    boiler.boil()
    boiler.drain()

    # will return the existing instance
    boiler2 = ChocolateBoiler()
    assert boiler == boiler2
