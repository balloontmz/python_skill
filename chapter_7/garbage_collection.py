#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
## 如何在环状数据结构中管理内存--弱引用

"""

__author__ = 'tomtiddler'

import sys
import weakref

"""
class A(object):
    def __del__(self):
        print("in __del__")


a = A()
print(sys.getrefcount(a) - 1) 
del a
print(sys.getrefcount(a))  # a被删除了  没有引用计数

"""


class Data(object):
    def __init__(self, value, owner):
        self.owner = weakref.ref(owner)  # self.owner = owner # 改进循环引用  weakref.ref 返回一个可调用对象，不增加引用计数
        self.value = value

    def __str__(self):
        return "%s's data, value is %s" % (self.owner(), self.value)

    def __del__(self):
        print("del data")


class Node(object):
    def __init__(self, value):
        self.data = Data(value, self)

    def __del__(self):
        print("del Node")


if __name__ == "__main__":
    node = Node(100)
    print(sys.getrefcount(node))
    del node
    # # 循环引用过程中的强制回收垃圾
    # import gc
    # gc.collect()
    input("wait...")  # del函数没有被调用，也就是没有进行垃圾回收。因为其循环引用导致的引用计数不为零


