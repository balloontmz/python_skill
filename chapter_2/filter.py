#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
获取列表中指定筛选条件的子列表
"""

__author__ = 'tomtiddler'

import timeit
from random import randint

data = [randint(-10, 10) for _ in range(10)]


def get_filter():
    return filter(lambda x: x >= 0, data)


def get_list():
    return [x for x in data if x >= 0]


def get_for():
    res = []
    for x in data:
        if x >= 0:
            res.append(x)
    return res


if __name__ == "__main__":
    # 时间测试 filter<list<for
    print(timeit.timeit(get_filter))
    print(timeit.timeit(get_list))
    print(timeit.timeit(get_for))

    print(list(filter(lambda x: x >= 0, data)))
    print([x for x in data if x >= 0])
    # print(timeit.timeit(stmt="[x for x in [1, 3, -2, -1] if x >= 0]"))


