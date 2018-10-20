#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
链式调用小练习，没事温习下链表吧。
"""

__author__ = 'tomtiddler'


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        if path == "users":
            self._path = self._path + "/" + path
            return lambda x: Chain('%s/%s' % (self._path, x))
        return Chain('%s/%s' % (self._path, path))  # 提供了链式调用的思想，递归地生成实例，并不是简单的字符串拼接

    def __str__(self):
        return self._path

    __repr__ = __str__


if __name__ == "__main__":
    print(Chain().users('michael').repos)

