#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

from random import randint
from itertools import chain

chinese = [randint(60, 100) for _ in range(40)]

english = [randint(60, 100) for _ in range(40)]

math = [randint(60, 100) for _ in range(40)]

c1, c2, c3 = [[randint(60, 100) for _ in range(40)] for _ in range(3)]

if __name__ == "__main__":
    # 并行迭代
    # 采用索引进行迭代，但不是所有数据类型都支持此种方法
    for i in range(len(chinese)):
        print(chinese[i] + english[i] + math[i])

    # zip 如果合并的多个列表长度不一致，取最短的列表长度, 惰性的迭代器
    combine = zip(chinese, english, math)
    for c, n, m in combine:
        print(c + n + m)

    # 串行迭代,chain  将列表串联起来
    count = 0
    for s in chain(c1, c2, c3):
        if s > 90:
            count += 1
    print(count)
