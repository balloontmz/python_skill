#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
词屏分析和统计  Counter
"""

__author__ = 'tomtiddler'

import re
from random import randint
from collections import Counter

data = [randint(0, 20) for _ in range(100)]

c = dict.fromkeys(data, 0)
# c = dict.fromkeys(range(0, 21), 0)  # 此处注意需要包括20

for x in data:
    c[x] += 1

c2 = Counter(data)

txt = open("doc.txt", "r").read()
c3 = Counter(re.split("\W+", txt))

if __name__ == "__main__":
    print(c)
    print(c2)
    print(c2.most_common(3))

    print(c3)
    print(c3.most_common(10))

