#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
寻找多个字典中的公共键
"""

__author__ = 'tomtiddler'

from functools import reduce
from random import randint, sample
import timeit

sample("abcdefg", randint(3, 6))  # 随机取样三到六个

s1 = {x: randint(1, 4) for x in sample("abcdefg", randint(3, 6))}

s2 = {x: randint(1, 4) for x in sample("abcdefg", randint(3, 6))}

s3 = {x: randint(1, 4) for x in sample("abcdefg", randint(3, 6))}


def get_for():
    res = []
    for key1 in s1:
        for key2 in s2:
            if key1 == key2:
                res.append(key1)
    return res


def get_common():
    return s1.keys() & s2.keys()


if __name__ == "__main__":
    print(s1, s2, s3)

    # 以下两种方法功能基本相同
    print(get_for())
    print(s1.keys() & s2.keys())
    print(timeit.timeit(get_for))
    print(timeit.timeit(get_common))  # 此方法时间明显低与迭代。
    # 多个字典的公共键
    print(reduce(lambda a, b: a & b, map(dict.keys, [s1, s2, s3])))

