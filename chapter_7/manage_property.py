#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
如何创建可管理的对象属性
在面向对象编程中，我们把方法（函数）看作对象的接口，直接访问对象的属性可能是不安全的，
或设计上不够灵活，但是使用调用方法在形式上不如访问属性简洁。python提供简单的调用方法
设置属性的功能
"""

__author__ = 'tomtiddler'

from math import pi


# 最简单的方法，采用定义方法 进行参数检查 以及定义一个property函数实例类似
class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("wrong type. ")
        self.radius = value

    def get_area(self):
        return self.radius ** 2 * pi

    r = property(get_radius, set_radius)


# 采用property装饰器，和定义一个property函数实例类似
class Circle2(object):
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

    def get_area(self):
        return self.radius ** 2 * pi


if __name__ == "__main__":
    c = Circle(3.2)
    # c.set_radius("abc")  # 报错

    print(c.r)  # 采用 property 函数定义一个可访问元素

    c2 = Circle2(3.2)
    c2.radius = 3.3  # 采用property装饰器的方法

