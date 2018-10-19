#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

s1 = "abcdefg"
s2 = "123456"

# 三个普通方法
s = s1 + s2
s3 = str.__add__(s1, s2)

l = [s1, s2]
s4 = ""
for p in l:
    s4 += p

# str.join  防止内存空间浪费
print("".join((str(x) for x in l)))  # 采用生成器（惰性）防止空间浪费，同时将可能是数字的项转换为字符串


