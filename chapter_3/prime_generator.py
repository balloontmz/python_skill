#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

from collections import Iterable, Iterator


class PrimeNumbers(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_prime_num(self, k):
        """采用的遍历方法，推测可使用筛选器的方法迭代取值--针对大范围并且开始值下标较小的情况"""
        if k < 2:
            return False
        for i in range(2, k):
            if k % i ==0:
                return False
        return True

    def __iter__(self):
        """返回一个可被next调用的对象"""
        for k in range(self.start, self.end+1):
            if self.is_prime_num(k):
                yield k


if __name__ == "__main__":
    for x in PrimeNumbers(1, 100):
        print(x)
    print(PrimeNumbers(1, 100).__iter__())
    print(PrimeNumbers(1, 100))
    x = PrimeNumbers(1, 100)
    # 类内实现了生成器，如果生成器定义在__iter__函数中，将是可迭代对象,同时，该函数定义的生成器是一个迭代器
    # 类内__iter__方法实现了生成器，其本身只是可迭代对象，并不是迭代器
    # 生成器的__iter__方法调用是其本身，迭代器的该方法好像也是其本身
    print(isinstance(x, Iterable))  # True
    print(isinstance(x, Iterator))  # False
    print(isinstance(x.__iter__(), Iterator))  # True
    print(x.__iter__().__iter__())  # x.__iter__ object


