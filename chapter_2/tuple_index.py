#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
采用下标或者命名元组进行访问
"""

__author__ = 'tomtiddler'

from collections import namedtuple

# 通常需要采用下标访问元素
student = ("Jim", 18, "male", "tomtiddler@163.com")
# 1.采用常量定义
NAME, AGE, SEX, EMAIL = range(4)
# 2.采用nametuple
Student = namedtuple("Student", ["name", "age", "sex", "email"])
s = Student("Jim", 18, "male", "tomtiddler@163.com")


if __name__ == "__main__":
    print(student[NAME], student[AGE])
    print(s.name, s.age)
    print(isinstance(s, tuple))

