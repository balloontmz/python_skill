#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

from itertools import islice

# 文本进行切片，无法直接切片，采用readlines会全部导入内存，占空间。引入迭代器 itertools.islice
f = open("doc.txt", "r")
lis = f.readlines()
print(lis[1:3])
f.close()

# 优化后的方法--
# 迭代其实是从下标0开始的，但是被islice抛弃了，并且会消耗迭代对象(对惰性迭代器而言，显式的可迭代对象不会)，
# 下次迭代将会从islice迭代完的地方开始。所以每次用完slice，记得重新声明迭代器
with open("doc.txt", "r") as fi:
    for line in islice(fi, 1, 5):
        print(line)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = iter(l)  # 惰性的迭代器对象
for x in islice(t, 2, 5):
    print(x)
print("-"*20)
for x in t:
    print(x)

