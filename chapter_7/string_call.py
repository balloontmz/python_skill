#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
三个类都有一个获取图形面积的接口，但接口名字不同，
我们可以实现一个统一的获取面积的函数，使用每种方法
名进行尝试，调用相应类的接口
方法一：
使用内置函数 getattr ， 通过名字在实例上获取方法对象
方法二：
使用标准库 operator 下的 methodcaller 函数调用
"""

__author__ = 'tomtiddler'

from operator import methodcaller


class Circle(object):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * 3.14


class Triangle(object):  # s三角形
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getArea(self):
        a, b, c = self.a, self.b, self.c
        p = (a + b + c)/2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return area


class Rectangle(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_area(self):
        return self.w * self.h


def get_area(shape):
    for name in ("area", "get_area", "getArea"):
        # f = getattr(shape, name, None)
        # if f:
        if getattr(shape, name, None):
            return methodcaller(name)(shape)
            # return f()


if __name__ == "__main__":
    shape1 = Circle(2)
    shape2 = Triangle(3, 4, 5)
    shape3 = Rectangle(6, 4)

    shapes = [shape1, shape2, shape3]
    print(list(map(get_area, shapes)))


