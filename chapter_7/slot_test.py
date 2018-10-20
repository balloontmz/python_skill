#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
某网络游戏中，定义了玩家类palyer（id， name， status）
每有一个在线玩家，在服务器程序内则有一个player的实例，
当在线人数很多时，将产生大量实例。
如何降低这些大量实例的内存开销？

定义类的`__slot__`属性，它来声明实例属性名字的列表
"""

__author__ = 'tomtiddler'

import sys


class Player(object):
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level


class Player2(object):
    __slots__ = ["uid", "name", "status", "level"]

    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level


p1 = Player(10001, "jim")
p2 = Player2(10001, "jim")

s = set(dir(p1)) - set(dir(p2))  # {'__weakref__', '__dict__'}  弱引用相关 以及 动态绑定所用的字典
s2 = set(dir(p2)) - set(dir(p1))  # {'__slots__'}

print(p1.__dict__)  # {'uid': 10001, 'name': 'jim', 'status': 0, 'level': 1}
p1.__dict__["y"] = 99
print(p1.y)  # 动态绑定 p2无法动态绑定

print(sys.getsizeof(p1.__dict__))  # 368  很大的一个字典了，对于每个实例来说，非常耗费内存空间
print(sys.getsizeof(p1))  # 56  实例本身大小并不大，以此推测，实例的相关属性保存的是指针。
print(sys.getsizeof(p2))  # 72
print(sys.getsizeof(p2.__slots__))  # 96

if __name__ == "__main__":
    pass

