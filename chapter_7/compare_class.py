#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
对类进行比较，需要实现以下方法
__lt__, __le__,__gt__,__eq__,__ne__
total_ordering  只需要定义一个等于  和一个 比较大小的函数
"""

__author__ = 'tomtiddler'

from functools import total_ordering
from abc import abstractmethod  # 子类必须重载该装饰器装饰的函数


# 为了防止多个类中同时要进行运算符的重载，我们可以定义一个抽象的基类，将比较运算封装起来
@total_ordering
class Shape(object):

    @abstractmethod
    def area(self):
        pass

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()


class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("wrong type. ")
        self._radius = value

    def area(self):
        return self._radius ** 2 * 3.14


class Rectangle2(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h



@total_ordering
class Rectangle(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()


if __name__ == "__main__":
    r1 = Rectangle(5, 3)
    r2 = Rectangle(4, 4)
    c3 = Circle(6)
    print(r1 < r2)  # 等同于调用r1.__lt__(r2)
    print(r1 > r2)
    print(r1 > c3)  # 由于r1定义了比较函数，所以可以进行比较

    # 为了防止多个类中同时要进行运算符的重载，我们可以定义一个抽象的基类，将比较运算封装起来
    # 以下的两个类都继承自基类Shape
    r3 = Rectangle2(5, 4)
    c4 = Circle(5)
    print(c4 > r3)
    print(c4 == r3)
