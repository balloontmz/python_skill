#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
如何采用文件描述符对实例属性进行检查
推测 flask 的字段类就是采用的此方法。
首字母大写的函数：使用str.capitalize()函数将字符串的首字母转为大写，其余变为小写
"""

__author__ = 'tomtiddler'


class Description(object):
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def __get__(self, instance, owner):
        print("in __get__", instance, owner)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print("in __set__", instance, value)
        if not isinstance(value, self.type_):
            raise TypeError("excepted an %s" % self.type_)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print("in __delect__", instance)
        del instance.__dict__[self.name]


class Person(object):
    name = Description("name", str)
    age = Description("age", int)
    height = Description("height", float)


if __name__ == "__main__":
    p = Person()
    p.name = "bob"
    print(p.name)
    # p.name = 17  # 会报错 参数检查

