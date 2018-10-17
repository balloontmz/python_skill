#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
获取集合中指定筛选条件的子集合
"""

__author__ = 'tomtiddler'

from random import randint
import timeit

data = [randint(-10, 10) for _ in range(10)]

s = set(data)


def get_filter():
    return {x for x in s if x % 3 == 0}


if __name__ == "__main__":
    print(get_filter())
    print(timeit.timeit(get_filter))

