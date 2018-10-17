#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
## 如何进行反向迭代以及如何实现反向迭代
l = [1, 2, 3, 4, 5]

l.reverse()  # 列表反置，改变原列表
l2 = l[::-1]  # 生成一个新的反置列表，耗费内存空间
reversed(l)  # 内置函数，产生一个列表的反向迭代器。惰性的。
"""

__author__ = 'tomtiddler'


class FloatRange(object):
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


if __name__ == "__main__":
    for x in FloatRange(1.0, 4.0, 0.5):
        print(x)
    for x in reversed(FloatRange(1.0, 4.0, 0.5)):  # 等同于 FloatRange(1.0, 4.0, 0.5).__reversed__()
        print(x)


