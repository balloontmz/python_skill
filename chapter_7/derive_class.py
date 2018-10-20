#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
如何派生内置不可变类型并修改其实例化行为
"""

__author__ = 'tomtiddler'


class IntTuple(tuple):
    def __new__(cls, iterable, *args, **kwargs):
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)

    def __init__(self, iterable):
        # before
        super(IntTuple, self).__init__()
        # after


if __name__ == "__main__":
    t = IntTuple([1, -1, "abc", ["x", "y"], 3, 6])
    print(t)

