#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
按字典某一项的值进行排序
"""

__author__ = 'tomtiddler'

from random import randint

student = {x: randint(50, 100) for x in "xyzabc"}

sor = sorted(zip(student.values(), student.keys()))

sor2 = sorted(student.items(), key=lambda x: x[1])

sor3 = sorted(student.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    print(sor)
    print(sor2)
    # 降序排列
    print(sor3)

