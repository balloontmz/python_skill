#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
寻找字典中值value大于某个数值的子字典
"""

__author__ = 'tomtiddler'

import timeit
import copy
from random import randint

student = {x: randint(50, 100) for x in range(1, 101)}


def get_dict():
    return {k: v for k, v in student.items() if v > 90}


def get_for():
    res = {}
    for k, v in student.items():
        if v > 90:
            res[k] = v
    return res


# 此法不十分非常可取，
def get_pop():
    res = copy.copy(student)
    for k, v in student.items():
        if v <= 90:
            res.pop(k)
    return res


if __name__ == "__main__":
    print(student)
    print(get_dict())
    print(timeit.timeit(get_dict))

    print(get_for())
    print(timeit.timeit(get_for))

    print(get_pop())
    print(timeit.timeit(get_pop))

